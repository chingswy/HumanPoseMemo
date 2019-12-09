- :two: Leeds Sports Pose Dataset  [[page](http://sam.johnson.io/research/lsp.html)]

    This dataset contains 2000 pose annotated images of mostly sports people.

    The file joints.mat is a MATLAB data file containing the joint annotations in a 3x14x2000 matrix called 'joints' with x and y locations and a binary value indicating the visbility of each joint.

    The ordering of the joints is as follows: 

    | number | name |
    | --- | --- |
    | 1 |    Right ankle |
    | 2 |    Right knee |
    | 3 |    Right hip|
    | 4 |    Left hip|
    | 5 |    Left knee |
    | 6 |   left ankle |
    | 7 |    Right wrist |
    | 8 |    Right elbow |
    | 9 |    Right shoulder|
    | 10 |    Left shoulder|
    | 11 |    Left elbow|
    | 12 |    Left wrist|
    | 13 |    Neck|
    | 14 |    Head top|

- :two: Leeds Sports Pose Extended Training Dataset [[page](http://sam.johnson.io/research/lspet.html)] 
    This dataset contains 10,000 images.

    The file joints.mat is a MATLAB data file containing the joint annotations in a 3x14x10000 matrix called 'joints' with x and y locations and a binary value indicating the visbility of each joint.

- :two: :couple:  coco  [[page](http://cocodataset.org/#home)]

    | No. | Name |
    | --- | --- |
    | 0 | nose |
    | 1 | left_eye |
    | 2 | right_eye |
    | 3 | left_ear |
    | 4 | right_ear |
    | 5 | left_shoulder |
    | 6 | right_shoulder |
    | 7 | left_elbow |
    | 8 | right_elbow |
    | 9 | left_wrist |
    | 10 | right_wrist |
    | 11 | left_hip |
    | 12 | right_hip |
    | 13 | left_knee |
    | 14 | right_knee |
    | 15 | left_ankle |
    | 16 | right_ankle |

- :two: MPII Human Pose Dataset [[page](http://human-pose.mpi-inf.mpg.de/)]

    The dataset includes around 25K images containing over 40K people with annotated body joints.

    Overall the dataset covers 410 human activities and each image is provided with an activity label.

    Annotations are stored in a matlab structure RELEASE having following fields

    - `.annolist(imgidx)` - annotations for image imgidx
        - `.image.name` - image filename
        - `.annorect(ridx)` - body annotations for a person ridx
            - `.x1, .y1, .x2, .y2` - coordinates of the head rectangle
            - `.scale` - person scale w.r.t. 200 px height
            - `.objpos` - rough human position in the image
            - `.annopoints.point` - person-centric body joint annotations
                - `.x, .y` - coordinates of a joint
                - `id` - joint id 
                - `is_visible` - joint visibility
        - `.vidx` - video index in video_list
        - `.frame_sec` - image position in video, in seconds
    - `img_train(imgidx)` - training/testing image assignment
    - `single_person(imgidx)` - contains rectangle id ridx of sufficiently separated individuals
    act(imgidx) - activity/category label for image imgidx
        - `act_name` - activity name
        - `cat_name` - category name
        - `act_id` - activity id
    - `video_list(videoidx)` - specifies video id as is provided by YouTube. To watch video on youtube go to https://www.youtube.com/watch?v=video_list(videoidx)

    | No | Name |
    | --- | --- |
    | 0  |  r ankle |
    |  1  |  r knee |
    |  2  |  r hip |
    |  3  |  l hip |
    |  4  |  l knee |
    |  5  |  l ankle |
    |  6  |  pelvis |
    |  7  |  thorax |
    |  8  |  upper neck |
    |  9  |  head top |
    |  10  |  r wrist |
    |  11  |  r elbow |
    |  12  |  r shoulder |
    |  13  |  l shoulder |
    |  14  |  l elbow |
    |  15  |  l wrist |

- :two: lsp-mpii-ordinal [[page](https://www.seas.upenn.edu/~pavlakos/projects/ordinal/)]

  This code seems to train model with relative relationship in PyTorch :[It's all Relative: Monocular 3D Human Pose Estimation from Weakly Supervised Data](http://www.vision.caltech.edu/%7Emronchi/projects/RelativePose/), see from the issue of the repo [ordinal-pose3d](https://github.com/geopavlakos/ordinal-pose3d).

- :three: h36m :three: [[page](http://vision.imar.ro/human3.6m/description.php)]


    • 3.6 million 3D human poses and corresponding images
    
    • 11 professional actors (6 male, 5 female)
    
    • 17 scenarios (discussion, smoking, taking photo, talking on the phone...)



|Num | Name | Children |
| ------- | ------- | ------- |
| 1 | root | 2  5  8 |
| 2 | lhipjoint | 3 |
| 3 | lfemur | 4 |
| 4 | ltibia |  |
| 5 | rhipjoint | 6 |
| 6 | rfemur 股骨 | 7 |
| 7 | rtibia 胫骨 |  |
| 8 | spine | 9 |
| 9 | thorax | 10  12  15 |
| 10 | jaw | 11 |
| 11 | head |  |
| 12 | lclaivcle 锁骨 | 13 |
| 13 | lhumerus 肱骨 | 14 |
| 14 | lhand |  |
| 15 | rclavicle | 16 |
| 16 | rhumerus | 17 |
| 17 | rhand |  |

- :three: up3d :three: [[page](http://files.is.tuebingen.mpg.de/classner/up/)]

  in the up3d dataset, the file is

  - 00000_body.pkl: ['rt', 'j2d', 'f', 'pose', 'betas', 't', 'trans']
  - 00000_dataset_info.txt: lsp 1,指定是在哪个数据集里面操作的
  - 00000_fit_crop_info.txt: 不知道这个crop信息具体指的是什么坐标
  - 00000_image.png:图片文件
  - 00000_joints.npy,关节,3x14

  train.txt,test.txt,trainval.txt,val.txt存放图片路径

  

- mpi_inf_3dhp :three:

- :three: MoSH
  [[page](http://mosh.is.tue.mpg.de/)]

- MoCap [[page](http://mocap.cs.cmu.edu/)]

- :three: surreal 
  [[Project page\]](http://www.di.ens.fr/willow/research/surreal/) [[arXiv\]](https://arxiv.org/abs/1701.01370)

| name | type | meaning|
| ------- | ------- | ------- |
|     camDist    |  [1 single]    |  - camera distance|
|     camLoc      | [3x1 single]  |  - camera location|
|     gender     |  [Tx1 uint8]    | - gender (0: 'female', 1: 'male')|
|     joints2D   |  [2x24xT single] |- 2D coordinates of 24 SMPL body joints on the image pixels|
|     joints3D  |   [3x24xT single] |- 3D coordinates of 24 SMPL body joints in real world meters|
|    pose       |  [72xT single]  | - SMPL parameters (axis-angle)|
|     shape     |   [10xT single]   |- body shape parameters|
|     zrot       |  [Tx1 single]   | - rotation in Z (euler angle)|
The [code](https://github.com/htung0101/3d_smpl) for the paper: Hsiao-Yu Fish Tung, Hsiao-Wei Tung, Ersin Yumer, Katerina Fragkiadaki, [Self-supervised Learning of Motion Capture](https://arxiv.org/abs/1712.01337), NIPS2017 (Spotlight)
show how to use surreal dataset.

- AI challenger keypoint dataset
:two:
[[web page](https://challenger.ai/dataset/keypoint)]
[[paper](https://arxiv.org/abs/1711.06475)]

| 1/右肩  | 2/右肘  | 3/右腕  | 4/左肩  | 5/左肘  |
| ------- | ------- | ------- | ------- | ------- |
| 6/左腕  | 7/右髋  | 8/右膝  | 9/右踝  | 10/左髋 |
| 11/左膝 | 12/左踝 | 13/头顶 | 14/脖子 |         |



- SMPL advanced

| Num | Name |
| ------- | ------- |
| 0	|Right ankle|
|    1| Right knee|
|    2| Right hip|
|    3| Left hip|
|    4| Left knee|
|    5| Left ankle|
|    6| Right wrist|
|    7| Right elbow|
|    8| Right shoulder|
|    9| Left shoulder|
|    10| Left elbow|
|    11| Left wrist|
|    12| Neck|
|    13| Head top|
|    14| nose|
|    15| left_eye|
|    16| right_eye|
|    17| left_ear |
|    18| right_ear |

```c
enum Part
    {
        BODY,   // 0
        LLEG,   // 1
        RLEG,   // 2
        LTORSO,    // 3
        LKNEE,  // 4
        RKNEE,  // 5
        MTORSO,  // 6
        LFOOT,  // 7
        RFOOT,  // 8
        UTORSO, // 9
        LLFOOT, // 10
        RRFOOT, // 11
        NECK,   // 12
        LSHOULDER,  // 13
        RSHOULDER,  // 14
        HEAD,   // 15
        LSHOULDER2, // 16
        RSHOULDER2, // 17
        LELBOW, // 18
        RELBOW, // 19
        LWRIST, // 20
        RWRIST, // 21
        LFINGERS, // 22
        RFINGERS, // 23
        TRANS, // 24
    };
```
