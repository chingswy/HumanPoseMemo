## SMPL: A Skinned Multi-Person Linear Model

![1539784197807](assets/1539784197807.png)



**摘要**：这篇文章提出了一个使用`pose`和`shape`参数驱动的线性的人体模型，模型的主要参数有：`rest pose template`,`blend weights`,`pose-dependent blend shapes`,`identity-dependent blend shapes`,和一个从vertices到joint的`regressor`，这些参数都是是从训练数据中学习得来的。与之前的工作不同的是，`pose-dependent blend shapes`这一项是pose旋转矩阵的线性函数。这样使得从一个大型数据集里面训练这个模型成为可能的。

**关键词**：Body shape, skinning（不重要）,blendshapes,soft-tissue(不重要)

**项目地址**：[SMPL](http://smpl.is.tue.mpg.de/)

### 导论

他们的目标是创造一个可以表示不同形状的身体的，可以随着动作自然的变形的，并且软组织在运动过程中还能发生形变的 人体模型。一般商业上的操作手法是手动操作mesh，来修改使用传统模型时出的问题。人的工作量就比较大。也有人从扫描的人体数据集中学习一个统计的身体模型，但是与商用软件不兼容，没法使用。

因此SMPL模型的目标就是，既能使用，又能表示大范围的人体，还要能通过pose来自然的形变，还要有软组织的动力学，做动画的效率高，并且和现有的渲染引擎兼容。

现有的LBS模型是使用得最广泛的，他是建立vertices和骨架之间的关系。但是这个模型会出现一些问题。

### 模型定义

模型与SCAPE类似，将身体形状分解为identity-dependent shape和non-rigid pose dependent shape。这个人体模型包含了$N=6890$个点，与$K=23$个关节。男女的大部分参数都是通用的。

模型的输入参数为形状参数$\beta$，和动作参数$\theta$,模型中包含以下几项：

- $\bar{\textbf{T}} \in \mathbb{R}^{3N}$ ,平均的模板形状 (mean template shape)

  这个时候的pose是zero pose,($\vec{\theta^*}$)

- $\mathcal{W}\in \mathbb{R}^{N\times K}$ ,各个关节的混合权重

- $B_S(\vec{\beta}):\mathbb{R}^{|\vec{\beta}|} \mapsto \mathbb{R}^{3N}$ ,blend shape函数，将shape参数映射到每一个点上

- $J(\vec{\beta}):\mathbb{R}^{|\vec{\beta}|} \mapsto \mathbb{R}^{3K}$ ，将shape参数映射到每个joint的位置上

- $B_P(\vec{\theta}):\mathbb{R}^{|\vec{\theta}|} \mapsto \mathbb{R}^{3N}$ ,将pose参数映射到每个点上

最终得到的结果就是$M(\vec{\beta},\vec{\theta};\Phi):\mathbb{R}^{|\vec{\theta}|\times |\vec{\beta}|} \mapsto \mathbb{R}^{3N}$ ,将shape和pose参数映射到每个点上。这里的$\Phi$ 指的是学习的模型的参数。

### 模型参数

pose参数是使用axis-angle来定义的，对于每一个joint，都有一个$\vec{\omega}_k\in \mathbb{R}^3$，然后加上原点处的，总共24个关节，就有72个参数。旋转矩阵是使用Rodrigues formula计算得到

$W(\bar{\mathbf{T}},\mathbf{J},\vec{\theta},\mathcal{W}):\mathbb{R}^{2N\times 3K\times|\vec{\theta}|\times |\mathcal{W}|} \mapsto \mathbb{R}^{3N}$ ,将rest pose、joint location、pose参数、blend weights权重转化成每个点的坐标量。

![1539784149245](assets/1539784149245.png)



### 代码实现

原始的代码是基于 [chumpy](https://github.com/mattloper/chumpy) 实现的，这个库似乎已经没有人维护了。而且也没法进行GPU计算。

模型参数：

| name | type | size|
| --- | --- | --- |
| J_regressor_prior     | <class 'scipy.sparse.csc.csc_matrix'>     | (24, 6890)|
| pose                  | <class 'chumpy.ch.Ch'>                    | (72,)|
| f                     | <type 'numpy.ndarray'>                    | (13776, 3)|
| J_regressor           | <class 'scipy.sparse.csc.csc_matrix'>     | (24, 6890)|
| betas                 | <class 'chumpy.ch.Ch'>                    | (10,)|
| kintree_table         | <type 'numpy.ndarray'>                    | (2, 24)|
| J                     | <class 'chumpy.reordering.transpose'>     | (24, 3)|
| v_shaped              | <class 'chumpy.ch_ops.add'>               | (6890, 3)|
| weights_prior         | <type 'numpy.ndarray'>                    | (6890, 24)|
| trans                 | <class 'chumpy.ch.Ch'>                    | (3,)|
| v_posed               | <class 'chumpy.ch_ops.add'>               | (6890, 3)|
| weights               | <class 'chumpy.ch.Ch'>                    | (6890, 24)|
| vert_sym_idxs         | <type 'numpy.ndarray'>                    | (6890,)|
| posedirs              | <class 'chumpy.ch.Ch'>                    | (6890, 3, 207)|
| pose_training_info    | <type 'dict'>                             | 6|
| bs_style              | <type 'str'>                              | 3|
| v_template            | <class 'chumpy.ch.Ch'>                    | (6890, 3)|
| shapedirs             | <class 'chumpy.ch.Ch'>                    | (6890, 3, 10)|
| bs_type               | <type 'str'>                              | 7 |
| r                     | <type 'numpy.ndarray'>                    | (6890, 3) |


[SMPL的numpy及TensorFlow实现](https://github.com/CalciferZh/SMPL)

[hmr论文中SMPL的tf实现](https://github.com/blzq/tf_smpl)



## 
