## Ordinal Depth Supervision for 3D Human Pose Estimation

### 摘要

这篇文章想解决的问题是, 如果直接训练端到端的3D human pose估计的网络的话, 缺乏自然环境下的有标注的图片. 大多数的数据集都是在室内环境,使用`Motion Capture` 系统来完成, 数据集的多样性就远小于2D human pose了. 为了减小`(alleviate)`对精确的3D ground truth数据的需求, 这篇文章提出了一种使用关节相对深度的弱监督信号. 标注这个信息可以由人类来完成.  文章展示`(showcase)`了使用这种信号来进行训练卷积网络的有效性. 作者还增强了LSP和MPII两个数据集. 这样可以使得网络在non-studio环境下工作. 

### Contributions

- 使用了人体的相对深度信息
- 增强了两个数据集
- 把相对深度放在网络中训练,效果良好

### APPROACH

#### 深度估计

对于每一个joint, 预测其深度$z_i$, 给的数据是
$$
r_{i,j} = \begin{cases}
+1, i 比j更靠近\\
-1, j比i更靠近\\
0, 深度接近
\end{cases}
$$
这部分的ConvNet将图片作为输入, 并预测$N$个关节的深度$z_i$, 对于每一组,计算其loss如下
$$
\mathcal{L}_{i,j} = \begin{cases} 
\log (1+\exp(z_i-z_j)), &r_{(i,j)} = +1,\\
\log (1+\exp(-z_i+z_j)),& r_{(i,j)} = -1,\\
(z_i-z_j)^2, &r_{(i,j)} = +1,
\end{cases}
$$
直觉上看,如果i比j更靠近的话,也就是i的深度小于j的深度, 那么应该惩罚$z_i-z_j$ ,反之同样. 这样完整的表达式写为
$$
\mathcal{L}_{rank} = \sum_{(i,j)\in \mathcal{I}} \mathcal{L}_{i,j}
$$
这样写的话就不需要所有关节对的关系了. 只要有部分关节的相对深度,那么还是可以计算的.(这个表达式好难写啊) 但是网络可以学习到关节顺序的一致性`(consensus)` .

#### 坐标预测

前面的网络预测深度的时候, 顺便也预测一下2D坐标.坐标使用L2loss.
$$
\mathcal{L}_{keyp} = \sum_{n=1}^N ||w_n-\hat w_n||_2^2
$$
把ranking loss和regression loss结合起来, 就得到了训练这个端对端网络的loss
$$
\mathcal{L} = \mathcal{L}_{rank} + \lambda \mathcal{L}_{keyp},\lambda = 100
$$

#### Volumetric prediction

最近的工作喜欢预测Volumetric表达,而不是直接回归坐标. 这篇把输出分解为两个部分的监督(没说怎么分解的):图片平面和深度. 准确的说, 对于每个关节, ConvNet预测score maps $\Psi_n$ ,这个可以转化成概率分布,通过使用softmax操作$\sigma$ .因此,关节$n$ 为于位置$u = (x,y,z)$ 的概率为$p(u|n) = \sigma [\Psi_n]_u$ .因此两个概率分布可以使用sum-pooling来求得.
$$
p(x,y|n) = \sum_z p(u|n),\\
p(z|n) = \sum_{x,y}p(u|n)
$$
这样分解的好处是,即使我们没有完整的3D ground truth,依然可以监督这个网络. 两个方向上是独立的.
$$
z_n = \sum_z zp(z|n)
$$

#### Reconstruction component

重建部分需要完成的工作是输入2D keypoint的坐标，和相对深度测量，输出3D坐标。

![1534057414254](assets/1534057414254.png)

重建部分是一个多层感知机，使用了两个bilinear units。这个是A simple论文里面的方法。训练这部分使用的是MoCap的数据，把数据投影一下到2D平面，然后为了模拟真正的输入，使用投影的坐标和有噪音的关节深度，这样的话深度关系是可以保留的，它们的值也不必和真正的值一样。损失函数就使用3D坐标的 L2 距离.



![1534057533510](assets/1534057533510.png)

将重建部分与前面的预测部分连接起来。







## 论文实现

训练的时候batch size是4，学习率是2.5e-4，使用rmsprop优化。使用了正负30度的旋转，以及0.75-1.25的尺度，和翻转

重建部分的训练和那篇论文里的一样。batch size=64,learning rate = 2.5e-4

### Implement

- Hourglass

![1534927274184](assets/1534927274184.png)

add a fully connected layer at the end with N output.

add a fully connected layer at the end with $3N$ outputs for coordinate regression, add a $1\times 1$ convolutional layer to produce $N\times 64$ channels for the volumetric output.

adopt the coarse-to-fine

![1534927719065](assets/1534927719065.png)

```python

i
nter = 
(
    conv(3,64,7,7,2,2,3,3)
    BN,ReLU
    Res(64,128)
    MaxPooling(2,2,2,2)
    Res(128,128)
    Res(128,nFeats)
)
hg = hourglass(4,nFeats,inter)
ll = hg
ll = Res(nFeats,nFeats,ll) x nModules # nModules = 3
ll = lin(nFeats,nFeats,ll)

# predicted heatmaps
tmpOut = conv(nFeats,outputDim[i],1,1,1,1,0,0)(ll)

# add predictions back
ll_ = conv(nFeats,nFeats,1,1,1,1,0,0)(ll)
tmpOut_ = con(outputDimp[i],nFeats,1,1,1,1,0,0)(tmpOut)
inter = CAddTable()(inter,ll_,tmpOut_)


```

![1535002453462](assets/1535002453462.png)

![1535002467160](assets/1535002467160.png)



![1534995224518](assets/1534995224518.png)



- the first hourglass is effectively 2D heatmaps
- the second hourglass is volumetric
- the blue columns correspond to the heatmaps (intermediate supervision for the first hourglass, and in 3D form as the final output for the second hourglass )
- convolutional layers are implemented as residual modules with $3\times 3$ kernels. 
- the first layer is $7\times 7$ ,
- the first layer uses stride = 2, decreasing the resolution from $256\times 256$ to $128\times 128$ .

> The note of the original torch network
>
> - Main line
>   - Conv(3->64,7x7,2,2,3,3)
>   - BN,ReLU
>   - Res(64,128)
>   - MaxPool(2x2,2,2)
>     - Res(128,128)
>     - Res(128,128)
>     - Res(128,256)
>   - % 池化过后的这一条接到了后面

![1534928498876](assets/1534928498876.png)

* the input is a vector of size 3N( estimated 2D joint coordinates normalized in [-1,1], and predicted ordinal depth for N joints)
* batch normalization,ReLU,Dropout



### Training details

#### Datasets

LSP,MPII with ordinal depth annotations

- lsp-dataset_original
  - joints.mat: [‘joints’] 3 x 14 x 2000,around(500,500,0 or 1)
  - ordinal.mat:‘ord’: 2000 x 14 x 14
- mpii_upis1h
  - joints.mat: [‘joints’] 3 x 16 x 13030,around(50,50,0 or 1)
  - ordinal.mat:‘ord’: 13030 x 16 x 16

这关节数目都不一样,怎么进行监督的.

网络是怎么输出17个joints的? 没联系啊

难道又把H36M放进去进行训练了?



```python
For the ordinal depth annotations, for a pair (i,j):
- if ordinal(i,j) = -1, then depth(i) < depth(j)
- if ordinal(i,j) = 1, then depth(i) > depth(j)
- if ordinal(i,j) = 0, then depth(i) ~= depth(j)
- if ordinal(i,j) = nan, then no annotation exists
```

认为0.1是噪声允许范围内的



Human3.6M: 



- Mixed-training strategy

  - ordinal examples

    loss based on the human annotations

  - respective dataset

    based on the known ground truth

#### Training

```python
batch_size = 4
lr = 2.5e-4
rmsprop
```

Augmentation for rotation(\pm 30 degrees,scale(0.75-1.25),flipping

| duration | dataset                         |
| -------- | ------------------------------- |
| 300k     | Human3.6M only                  |
| 2.5M     | H3.6M and LSP+MPII Ordinal data |
| 1.5M     | HumanEva-I and LSP+MPII         |

#### Reconstruction

require MoCap data. simply project each 3D pose skeleton to the 2D image plane. To simulate the input, we use the projected 2D joint locations and a noisy version of the depth of the joints.
$$
\mathcal{L}_{3D} = \sum^N_{n=1} ||S_n-\hat S_n||^2_2
$$


```python
batch_size = 64
lr = 2.5e-4
rmsprop
iterations = 200k
```

#### flowchart

```python
# set up input image
img = load(img)
center,scale = load_annot(annot)
inp = crop(img,center,scale,0,256)


# get network output
outVol = m_ord(inp.view(1,3,256,256),scale)
flippedOutVol = m_ord(flip(inp.view(1,3,256,256)),scale)
outVol = (outVol+flippedOutVol)/2

# size 1x17x3
outOrd = getPreds3D(outVol)
outOrd = outOrd[0].transpose(1,2)
# size 1 x 3 x 17
pts = outOrd[1,2]
# 减掉中心
pass
# 除以最大值
pass

zind = (outOrd[3]-33)/32.0

# input rec
inp_rec(1:17) = pts(1)
inp_rec(18:34) = pts(2)
inp_rec(35:51) = zind

# view as 1x51
out3D = m_rec(inp_rec)
preds3D = torch.reshape(out3D,1,3,17).transpose(2,3)

```

![1535094757474](assets/1535094757474.png)



>  训练第二个网络的时候噪音使用了多大的没有说.

切一张图需要0.06s.

