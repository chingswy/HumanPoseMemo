1. [A Neural Network for Detailed Human Depth Estimation from a Single Image](https://arxiv.org/pdf/1910.01275.pdf): separate the depth map into a smooth base shape and a residual detail shape and designa network with two branches to regress them respectively.

2. [DenseRaC: Joint 3D Pose and Shape Estimation by Dense Render-and-Compare](https://arxiv.org/pdf/1910.00116.pdf): pixel-> IUV -> pose and shape

3. [Dense Intrinsic Appearance Flow for Human Pose Transfer](http://mmlab.ie.cuhk.edu.hk/projects/pose-transfer/):[code](https://github.com/ly015/intrinsic_flow) use SMPL model to generate pose transfer. 根据图片做了vertex matching，计算了flow与visibility

4. [Consensus-based Optimization for 3D Human Pose Estimation in CameraCoordinates](https://arxiv.org/pdf/1911.09245.pdf): estimate absolute 3D human pose, optimize camera parameters.

5. [Detailed Human Shape Estimation from a Single Imageby Hierarchical Mesh Deformation](http://openaccess.thecvf.com/content_CVPR_2019/papers/Zhu_Detailed_Human_Shape_Estimation_From_a_Single_Image_by_Hierarchical_CVPR_2019_paper.pdf): [code](https://github.com/zhuhao-nju/hmd): use deformation to solve a more detailed human model.

