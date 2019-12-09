

# DensePose: Dense Human Pose Estimation In The Wild

- 解决问题：建立RGB图像和人体surface-based的表示之间的密集对应关系
- 难点：存在背景、遮挡、姿态、尺度的变化
- 主要贡献：
  - 标注了一个新的数据集，基于COCO2014，增加了UV标注。50k张图
  - 设计了一个输入一张RGB图片输出UV坐标的网络框架，基于mask-rcnn
  - 设计了一个teacher网络，用来生成训练数据



## Estimation

- 任务：训练一个预测image pixels和surfacec points之间的对应关系的深层网络的任务。
- 将DenseReg方法与Mask-RCNN架构相结合来引入改进的架构
- 开发了DensePose-RCNN的cascading扩展，进一步提高准确性
- 基于训练的interpolation方法，将稀疏的监督信号变成更密集和更有效的变体

### Fully-convolutional dense pose regression

使用完全卷积网络(FCN)，结合了分类和回归任务，类似于DenseReg。由于人体结构复杂，因此我们将其分解为多个独立的部分，并使用局部二维coordinates系对每个部分进行参数化，以识别表面部分上任何节点的位置

1. 将pixel进行分类
2. 回归part pixel 的确切coordinates

### Region-based Dense Pose Regression

采用region-based的方法，其中包括ROI cascading，通过ROI-pooling提取区域自适应特征，并将结果特征提供给一个区域特定的分枝。这样的体系结构将任务的复杂性分解为可控模块，并通过ROI-pooling实现规模选择机制。同时他们也可以端到端的方式进行训练。

采用了Mask r-cnn的结构。（待看）

![1540110428399](assets/1540110428399.png)

### Multi-task cascaded architectures

![1540111318295](assets/1540111318295.png)

Cross-cascading architecture. 有多任务的时候，ROIAlign的输出输入到两个网络去，两个任务的第一阶段的输出又被组合到一起，然后给第二阶段的refinement.



## code
### UV

#### 训练数据

```python
dp_x,dp_y：人工标注者收集的点在图像中的空间坐标
dp_I:代表每个点所属的24块区域中的一块
dp_U,dp_V：UV空间中的坐标
```



对于三维模型的坐标系统，有两个坐标系统，一个是顶点的位置`(x,y,z)`，一个是`UV`坐标。
UV表示图片在显示器水平、垂直方向上的坐标，取值范围是0-1。

二维的UV坐标系，可以定位图像上的任意一个像素，由于模型表面贴图也是二维的，所以可以通过换算把表面上的点和平面图像上的像素对应起来。

https://computergraphics.stackexchange.com/questions/1866/how-to-map-square-texture-to-triangle

https://en.wikipedia.org/wiki/Barycentric_coordinate_system

### 原论文IUV2FBC实现
```python
def IUV2FBC(self,I,U,V)
    find Face indices == I
    select Face now
    P = [U,V,0]
    P_0 = [U_norm[:,0],V_norm[:,0],0]
    P_1 = [U_norm[:,1],V_norm[:,1],0]
    P_2 = [U_norm[:,2],V_norm[:,2],0]
    for P0,P1,P2 in P_0,1,2:
        if barycentric_coordinates_exists(P0,P1,P2,P)
            bc1,bc2,bc3 = barycentric_coordinates(P0,P1,P2,P)
            return FaceNow,bc1,bc2,bc3
    # if the found UV is not inside any faces,select the vertex that is closest
    
```


`UV_Processed.mat`

| Name            | Shape   |
| --------------- | ------- |
| All_FaceIndices | 13774x1 |
| All_Faces       | 13774x3 |
| All_U           | 7829x1  |
| All_U_norm      | 7829x1  |
| All_V           | 7829x1  |
| All_V_norm      | 7829x1  |
| All_vertices    | 1x7829  |

![1540115513175](assets/1540115513175.png)

```matlab
load('UV_Processed.mat')
plot(All_U,All_V,'.')
trimesh(All_Faces,All_U,All_V)
```



![1540121620988](assets/1540121620988.png)

代码中使用的时候是并不是使用原来的，而是使用norm过的来进行计算的，这样的每一片的值的范围都在0-1的范围内了。

![1540122227637](assets/1540122227637.png)

![1540122667300](assets/1540122667300.png)



其中第一个patch归一化之后是这样的。（这个颜色好迷啊，懒得指定了）

`UV_symmetry_transforms.mat`

| Name         | Shape     |
| ------------ | --------- |
| U_transforms | 1x24 cell |
| V_transforms | 1x24 cell |



我们想要实现的是对点的坐标可微，所以找到最近点这个过程虽然是不可微的。但是相当于这个是给定的数据，不需要改变，所以不需要可微，也能优化。那么整理一下的话就是，已经给定了这个对应关系，这些像素对应的是哪个位置已经可以确定了，barycentric的坐标相当于也是可以确定了的，那么改变的只是这些点的坐标，只要后面这部分是可微的就可以进行优化了。

而且对于这样一张给定的图，前面部分这些都可以先保存下来的，省的每次都要去找。

这个网络训练的时候有没有把不在范围内这个考虑为loss加进去？可以重新训练一下。










## related works

[Dense Pose Transfer](https://arxiv.org/abs/1809.01995)

