# DensePose

[Dense pose transfer]

[Holopose]

[Densebody]

[Denserac]

[Texturepose]





ICCV19: [Delving Deep Into Hybrid Annotations for 3D Human Recovery in the WildSupplemental Material](http://personal.ie.cuhk.edu.hk/~ccloy/files/iccv_2019_delving_supp.pdf)



CVPR20: [Transferring Dense Pose to Proximal Animal Classes](https://openaccess.thecvf.com/content_CVPR_2020/papers/Sanakoyeu_Transferring_Dense_Pose_to_Proximal_Animal_Classes_CVPR_2020_paper.pdf)

迁移到动物身上

CVPR20: [3D Human Mesh Regression with Dense Correspondence](https://openaccess.thecvf.com/content_CVPR_2020/papers/Zeng_3D_Human_Mesh_Regression_With_Dense_Correspondence_CVPR_2020_paper.pdf)

输入图像，输出IUV，使用参考的UV map，转换到UV map上，最后回归出location map



NIPS:[Correlated Uncertainty for LearningDense Correspondences from Noisy Labels]

[Making DensePose fast and light](https://arxiv.org/pdf/2006.15190.pdf)，[code](https://github.com/zetyquickly/DensePoseFnL)



















[Supervision by Registration and Triangulationfor Landmark Detection](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9050873)

**问题：** 人工标注数据不准确

**方法：** 通过无标记的多视角视频，提高检测器的精度和准确度

**动机：** 

1. 时序上，相邻帧的同一个标记点应该与registration一致，即光流
2. 视角上，多视角的同一个点应该对应同一个3D点，即多视角一致性

使用端到端的可训练模块。













[Capture Dense: Markerless Motion Capture Meets Dense Pose Estimation](https://arxiv.org/pdf/1812.01783v1.pdf)



[Slim DensePose: Thrifty Learning from Sparse Annotations and Motion Cues](https://arxiv.org/pdf/1906.05706.pdf)

[Supervision by Registration and Triangulationfor Landmark Detection]()








$$
(v\rightarrow e): h_{(i, j)}^{(l)} = \mathcal{N}_e([h_i^{(l-1)}, h_j^{(l-1)}, h_{(i,j)}^{(l-1)}])\\
(e\rightarrow v): h_i^{(l)} = \mathcal{N}_{2D}(h_{i,2D}^{(l)}) + \mathcal{N}_{track}(h_{(i,track)}^{(l)}) + \mathcal{N}_{cross}(h_{(i,cross)}^{(l)})\\
$$

- 边的更新直接使用连接的两个节点的特征，与边的特征

- 点的更新需要整合三种类型信息：

  - 2D信息：单张图像中，在人体骨架上连接的两个边。先实现一个不区分关节类型的，简简单单的MPN。
    $$
    h_{i,2D}^{(l)} = \sum_{j\in N_i}\mathcal{N}_{2D}([h_{i}^{(l-1)}, h_{i, j}^{(l-1)}, h_{i}^{(0)}])
    $$
    后面再考虑对于不同类型的关节，单独学习一个权重.这里的sum应该用均值代替。

  - 时序信息：一个时序边连接的是不同帧中，同一种类型的检测结果的不同实例。

  - 多视角信息：不同视角中，同一种类型的检测结果的不同实例。



PoseTrack数据：

训练：

1. detection：使用GT可见的
2. feature：使用superpoint模块
3. GT：使用GT标注信息

测试：

1. detection：使用GT /  使用OpenPose / 使用HRNet
2. feature：同训练

