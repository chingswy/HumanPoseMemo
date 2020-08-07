'''
    @ Date: 2020-07-08 15:51:29
    @ LastEditors: Qing Shuai
    @ LastEditTime: 2020-07-08 20:24:25
    @ Author: Qing Shuai
    @ Mail: s_q@zju.edu.cn
'''
from pybtex.database.input import bibtex
from utils import get_colors, readJson, to_hex

TAGS = {
    'mul': 'multi person',
    'mv': 'multi view',
    'sv':'single view',
    'pic': 'pictorial based',
    'part': 'part based',
    'smpl': 'smpl based',
    'uv': 'uv map based',
    'temp': 'temporal',
    'td': 'top down',
    'bu': 'bottom up',
    'dis': 'discriminator',
    'gen': 'generator',
    'vol': 'volume based'
}
width = 1
rgb = get_colors()
def main(args):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(args.inp)

    def sort_by_year(x):
        return int(x[1].fields['year'])
        
    bib_sorted = sorted(bib_data.entries.items(), key=sort_by_year)
    papers = []
    tags = {}
    for key, value in bib_sorted:
        print(key, value.fields['title'])
        papers.append(value.fields['title'])
        taglist = value.fields['swy'].split('.')
        taglist = [TAGS[tag] for tag in taglist]
        tags[value.fields['title']] = taglist
    
    with open(args.out, 'w') as f:
        f.writelines('var color = {\n')
        for i, human in enumerate(TAGS.values()):
            f.writelines("    '{}': \"{}\",\n".format(human, to_hex(rgb[i])))
        f.writelines("};\n")
        # write edges:
        f.writelines('var data = [\n')
        for i, human in enumerate(papers):
            for val in tags[human]:
                f.writelines("    ['{}', \"{}\", {}],\n".format(val, human, width))
        f.writelines("];\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--inp', type=str, default='expert/data/mvpose.bib')
    parser.add_argument('--out', type=str, default='expert/data/mvpose.js')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args() 
    main(args)