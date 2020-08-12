# HumanPoseMemo
Memo about 3D human pose estimation, record of datasets, papers, codes.

## Datasets

### [2D datasets](./datasets/2d.md)

<details>
  <summary><b>related works</b></summary>
  <div align="center">
    <img src="README.assets/1576828687165.png" width="300" alt="3DPW" align=center />
  </div>
  <p>

  - [Leeds Sports Pose Dataset](http://sam.johnson.io/research/lsp.html)
  - [Leeds Sports Pose Extended Training Dataset](http://sam.johnson.io/research/lspet.html)
  - [COCO](http://cocodataset.org/#home)
  - [MPII Human Pose Dataset](http://human-pose.mpi-inf.mpg.de/)
  - [lsp-mpii-ordinal](https://www.seas.upenn.edu/~pavlakos/projects/ordinal/)
  - [AI challenger keypoint dataset](https://challenger.ai/dataset/keypoint)
  - [CrowdPose](https://github.com/Jeff-sjtu/CrowdPose)
  - [OCHuman](https://github.com/liruilong940607/OCHumanApi)
  - [COCO-WholeBody](https://github.com/jin-s13/COCO-WholeBody)
  - [DensePose](http://densepose.org/)
  </p>
</details>

### [3D datasets](./datasets/3d.md)

<details>
  <summary><b>related works</b></summary>
  <div align="center">
    <img src="README.assets/1576828968571.png" width="300" alt="3DPW" align=center />
  </div>
  <p>

  - [Human3.6M](http://vision.imar.ro/human3.6m/description.php)
  - [Unit the People](http://files.is.tuebingen.mpg.de/classner/up/)
  - [mpi_inf_3dhp](http://gvv.mpi-inf.mpg.de/3dhp-dataset)
  - [CMU Panoptic Dataset](http://domedb.perception.cs.cmu.edu/)
  </p>
</details>


### [SMPL datasets](./datasets/smpl.md)

<details>
  <summary><b>related works</b></summary>
  <div align="center">
    <img src="README.assets/1576828885408.png" width="300" alt="3DPW" align=center />
  </div>
  <p>

  - [SURREAL](http://www.di.ens.fr/willow/research/surreal/)
  - [eft](https://github.com/facebookresearch/eft)
  </p>
</details>

### [Dressed datasets](./datasets/dress.md)
<details>
  <summary><b>related works</b></summary>
  <div align="center">
    <img src="README.assets/1576828885408.png" width="300" alt="3DPW" align=center />
  </div>
  <p>

  - [3DPeople: Modeling the Geometry of
        Dressed Humans](https://www.albertpumarola.com/research/3DPeople/index.html)
  </p>
</details>

### Face, Hands and Feet
<details>
  <summary><b>related works</b></summary>
  <p>
    
  - [FreiHAND: A Dataset for Markerless Capture of Hand Pose and Shape fromSingle RGB Images](https://lmb.informatik.uni-freiburg.de/projects/freihand/)
  </p>
</details>

## Papers
> note: I don't include some paper without codes.

### Monocular human pose estimation
<details>
  <summary><b>2020</b></summary>
  <p>

  - [Compressed Volumetric Heatmaps for Multi-Person 3D Pose Estimation](https://arxiv.org/abs/2004.00329):[[code](https://github.com/fabbrimatteo/LoCO)]
  - [Learning 3D Human Shape and Pose fromDense Body Parts](https://arxiv.org/pdf/1912.13344.pdf)
  - [CVPR 20, Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data](https://calciferzh.github.io/publications/zhou2020monocular):[[code](https://github.com/CalciferZh/minimal-hand)]
  - [CVPR 20, Hierarchical Human Parsing with Typed Part-Relation Reasoning](https://github.com/hlzhu09/Hierarchical-Human-Parsing):[[code](https://github.com/hlzhu09/Hierarchical-Human-Parsing)]
  - [CVPR 20, VIBE: Video Inference for Human Body Pose and Shape Estimation](https://github.com/mkocabas/VIBE)]
  - [CVPR 20, 3D Human Mesh Regression with Dense Correspondence](https://arxiv.org/pdf/2006.05734.pdf) [[code]](https://github.com/zengwang430521/DecoMR)
  </p>
</details>
<details>
  <summary><b>2019</b></summary>
  <p>

  - [CVPR, 19. Learning 3D Human Dynamics from Video](https://github.com/akanazawa/human_dynamics)
  - [ICCV, 19. TexturePose: Supervising Human Mesh Estimation with Texture Consistency](https://github.com/geopavlakos/TexturePose)
  - [ICCV, 19. SPIN - SMPL oPtimization IN the loop](https://github.com/nkolot/SPIN)
  - [ICCV, 19. Delving Deep Into Hybrid Annotations for 3D Human Recovery in the Wild](https://github.com/penincillin/DCT_ICCV-2019)
  - [ICCV, 19. Camera Distance-aware Top-down Approach for 3D Multi-person Pose Estimation from a Single RGB Image](https://github.com/mks0601/3DMPPE_ROOTNET_RELEASE)
  - [CVPR, 19. Exploiting temporal context for 3D human pose estimation in the wild](https://github.com/deepmind/Temporal-3D-Pose-Kinetics)
  - [CVPR, 19. Learning Joint Reconstruction of Hands and Manipulated Objects - Demo, Training Code and Models](https://github.com/hassony2/obman_train)
  - [ICCV, 19. MonoLoco: Monocular 3D Pedestrian Localization and Uncertainty Estimation](https://github.com/vita-epfl/monoloco)
  - [SIGGRAPH Asia, 18. Motion Reconstruction Code and Data for Skills from Videos (SFV)](https://github.com/akanazawa/motion_reconstruction)
  - [CVPR, 19. Monocular Total Capture: Posing Face, Body and Hands in the Wild](https://github.com/CMU-Perceptual-Computing-Lab/MonocularTotalCapture)
  - [CVPR, 19. Detailed Human Shape Estimation from a Single Image by Hierarchical Mesh Deformation](https://github.com/zhuhao-nju/hmd)
  - [CVPR, 19. Convolutional Mesh Regression for Single-Image Human Shape Reconstruction](https://github.com/nkolot/GraphCMR)
  - [CVPR, 19. Self-Supervised Learning of 3D Human Pose using Multi-view Geometry](https://github.com/mkocabas/EpipolarPose)
  - [CVPR, 19. 3D human pose estimation in video with temporal convolutions and semi-supervised training](https://github.com/facebookresearch/VideoPose3D)
  </p>
</details>
<details>
  <summary><b>2018</b></summary>
  <p>

  - [ECCV, 18. Integral Human Pose Regression](https://github.com/JimmySuen/integral-human-pose)
  - [CVPR, 18. End-to-end Recovery of Human Shape and Pose](https://github.com/akanazawa/hmr)
  - [CVPR, 18. Ordinal Depth Supervision for 3D Human Pose Estimation](https://github.com/geopavlakos/ordinal-pose3d)
  </p>
</details>

### Multi-view human pose estimation
<details>
  <summary><b>2020</b></summary>
  <p>

  </p>
</details>
<details>
  <summary><b>2019</b></summary>
  <p>

  - [ICCV, 19. Cross View Fusion for 3D Human Pose Estimation](https://github.com/microsoft/multiview-human-pose-estimation-pytorch)
  - [ICCV, 19. Shape-Aware Human Pose and Shape Reconstruction Using Multi-View Images](https://github.com/williamljb/HumanMultiView)
  - [ICCV, 19 Learnable Triangulation of Human Pose](https://github.com/karfly/learnable-triangulation-pytorch)
  - [CVPR, 19. Fast and Robust Multi-Person 3D Pose Estimation from Multiple Views](https://github.com/zju3dv/mvpose)

  </p>
</details>
<details>
  <summary><b>2018</b></summary>
  <p>

  - [CVPR, 17. Coarse-to-Fine Volumetric Prediction for Single-Image 3D Human Pose](https://github.com/geopavlakos/c2f-vol-train)
  - [3DV, 17. Towards Accurate Marker-less Human Shape and Pose Estimation over Time](https://github.com/YinghaoHuang91/MuVS)
  </p>
</details>


### Detailed human shape reconstruction
<details>
  <summary><b>2020</b></summary>
  <p>

  - [PIFuHD: Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization](https://shunsukesaito.github.io/PIFuHD/):[[code](https://github.com/shunsukesaito/PIFuHD)]
  </p>
</details>
<details>
  <summary><b>2019</b></summary>
  <p>

  - [ICCV 19, PIFu: Pixel-Aligned Implicit Function for High-Resolution Clothed Human Digitization](https://shunsukesaito.github.io/PIFu/):[[code](https://github.com/shunsukesaito/PIFu)]
  - [Learning Nonparametric Human Mesh Reconstruction from a Single Image without Ground Truth Meshes](https://arxiv.org/pdf/2003.00052.pdf)：image  => 2D pose + part seg ==Graph-CNN==> mesh
  - [PeelNet: Textured 3D reconstruction of human body using single view RGB image](https://arxiv.org/pdf/2002.06664.pdf)
  - [CVPR, 19. Dense Intrinsic Appearance Flow for Human Pose Transfer](https://github.com/ly015/intrinsic_flow)
  - [ICCV, 19. Liquid Warping GAN: A Unified Framework for Human Motion Imitation, Appearance Transfer and Novel View Synthesis](https://github.com/svip-lab/impersonator)
  - [CVPR, 19. Learning to Regress 3D Face Shape and Expression from an Image without 3D Supervision](https://github.com/soubhiksanyal/RingNet)
  - [ICCV, 19. Multi-Garment Net: Learning to Dress 3D People from Images](https://github.com/bharat-b7/MultiGarmentNetwork)
  </p>
</details>
<details>
  <summary><b>2018</b></summary>
  <p>

  - [3DV, 18. Detailed Human Avatars from Monocular Video.](https://github.com/thmoa/semantic_human_texture_stitching)
  - [CVPR, 18.  Learning to Reconstruct People in Clothing from a Single RGB Camera.](https://github.com/thmoa/octopus)
  - [CVPR, 18. Video based reconstruction of 3D people models.](https://github.com/thmoa/videoavatars)

  </p>
</details>

## Multi-View Stereo

<details>
  <summary><b>2020</b></summary>
  <p>

  - [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](http://www.matthewtancik.com/nerf): [[code](https://github.com/bmild/nerf)],[[code-PyTorch](https://github.com/yenchenlin/nerf-pytorch)]
  </p>
</details>

<details>
  <summary><b>2019</b></summary>
  <p>

  - [DeepPruner: Learning Efficient Stereo Matching via Differentiable PatchMatch](https://arxiv.org/pdf/1909.05845.pdf): [[code](https://github.com/uber-research/DeepPruner)]
  </p>
</details>

### Other
<details>
  <summary><b>2020</b></summary>
  <p>
    
  - [Learning Character-Agnostic Motion for Motion Retargeting in 2D](https://motionretargeting2d.github.io/)
    Decompose and recompose the video, could be used for motion retrival.
  </p>
</details>
<details>
  <summary><b>2019</b></summary>
  <p>

  - [CVPR, 19. SMPL-X: A new joint 3D model of the human body, face and hands together](https://github.com/vchoutas/smplx)
  - [CVPR, 17. Learning from Synthetic Humans (SURREAL)](https://github.com/gulvarol/surreal)
  - [BMVC, 18. Learning Human Optical Flow](https://github.com/anuragranj/humanflow)
  - [ICCV, 19. Resolving 3D Human Pose Ambiguities with 3D Scene Constraints](https://github.com/MohameHassan/prox)
  </p>
</details>
<details>
  <summary><b>2018</b></summary>
  <p>

  </p>
</details>

### [CVPR2020](http://cvpr2020.thecvf.com/program/main-conference)
keywords: human, motion, tracking, person, pose

#### 2D human pose
- Combining Detection and Tracking for Human Pose Estimation in Videos
- [MetaFuse: A Pre-trained Fusion Model for Human Pose Estimation](https://arxiv.org/pdf/2003.13239.pdf)
- HigherHRNet: Scale-Aware Representation Learning for Bottom-Up Human Pose Estimation
- The Devil Is in the Details: Delving Into Unbiased Data Processing for Human Pose Estimation
- Distribution-Aware Coordinate Representation for Human Pose Estimation
- Combining Detection and Tracking for Human Pose Estimation in Videos

#### monocular 3D pose

- Deep Kinematics Analysis for Monocular 3D Human Pose Estimation
- Attention Mechanism Exploits Temporal Contexts: Real-Time 3D Human Pose Reconstruction[oral, [code](https://github.com/lrxjason/Attention3DHumanPose)]
- Weakly-Supervised 3D Human Pose Learning via Multi-View Images in the Wild
- VIBE: Video Inference for Human Body Pose and Shape Estimation
- Coherent Reconstruction of Multiple Humans From a Single Image
- [Self-Supervised 3D Human Pose Estimation via Part Guided Novel Image Synthesis](https://arxiv.org/pdf/2004.04400.pdf)[oral, [project](https://sites.google.com/view/pgp-human)]
- [Cascaded Deep Monocular 3D Human Pose Estimation With Evolutionary Training Data]()[oral]
- [GHUM & GHUML: Generative 3D Human Shape and Articulated Pose Models]()[oral]
- [Generating 3D People in Scenes Without People]()[oral]
- [Bodies at Rest: 3D Human Pose and Shape Estimation From a Pressure Image Using Synthetic Data]()[oral]
- [Multiview-Consistent Semi-Supervised Learning for 3D Human Pose Estimation](https://arxiv.org/pdf/1908.05293.pdf)
- Optical Non-Line-of-Sight Physics-Based 3D Human Pose Estimation
- UniPose: Unified Human Pose Estimation in Single Images and Videos
- 3D Human Mesh Regression With Dense Correspondence
- Three-Dimensional Reconstruction of Human Interactions
- Sequential 3D Human Pose and Shape Estimation From Point Clouds
- Object-Occluded Human Shape and Pose Estimation From a Single Color Image[oral]
- PandaNet: Anchor-Based Single-Shot Multi-Person 3D Pose Estimation
- Compressed Volumetric Heatmaps for Multi-Person 3D Pose Estimation

#### multi view

- ActiveMoCap: Optimized Viewpoint Selection for Active Human Motion Capture
- Multi-View Neural Human Rendering
- Fusing Wearable IMUs With Multi-View Images for Human Pose Estimation: A Geometric Approach
- Cross-View Tracking for Multi-Human 3D Pose Estimation at Over 100 FPS
- 4D Association Graph for Realtime Multi-Person Motion Capture Using Multiple Video Cameras
- Deep 3D Capture: Geometry and Reflectance From Sparse Multi-View Images
- Lightweight Multi-View 3D Pose Estimation Through Camera-Disentangled Representation

#### depth, detailed, cloth

- PIFuHD: Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization
- Self-Supervised Human Depth Estimation From Monocular Videos
- ARCH: Animatable Reconstruction of Clothed Humans
- DeepCap: Monocular Human Performance Capture Using Weak Supervision
- TetraTSDF: 3D Human Reconstruction From a Single Image With a Tetrahedral Outer Shell
- Learning to Transfer Texture From Clothing Images to 3D Humans
- TailorNet: Predicting Clothing in 3D as a Function of Human Pose, Shape and Garment Style[oral]
- Novel View Synthesis of Dynamic Scenes With Globally Coherent Depths From a Monocular Camera
- 4D Visualization of Dynamic Events From Unconstrained Multi-View Videos
- Multi-View Neural Human Rendering


#### HH, HO interactions

- Discovering Human Interactions With Novel Objects via Zero-Shot Learning
- Mixture Dense Regression for Object Detection and Human Pose Estimation
- VSGNet: Spatial Attention Network for Detecting Human Object Interactions Using Graph Convolutions
- PPDM: Parallel Point Detection and Matching for Real-Time Human-Object Interaction Detection
- Learning Human-Object Interaction Detection Using Interaction Points
- Cascaded Human-Object Interaction Recognition
- GanHand: Predicting Human Grasp Affordances in Multi-Object Scenes
- Detailed 2D-3D Joint Representation for Human-Object Interaction

#### action, tracking, trajectory, prediction

- Dynamic Multiscale Graph Neural Networks for 3D Skeleton Based Human Motion Prediction
- Active Vision for Early Recognition of Human Actions
- Semantics-Guided Neural Networks for Efficient Skeleton-Based Human Action Recognition
- [Social-STGCNN: A Social Spatio-Temporal Graph Convolutional Neural Network for Human Trajectory Prediction][[code](https://github.com/abduallahmohamed/Social-STGCNN)]
- Reciprocal Learning Networks for Human Trajectory Prediction
- PaStaNet: Toward Human Activity Knowledge Engine
- A Stochastic Conditioning Scheme for Diverse Human Motion Prediction
- Bayesian Adversarial Human Motion Synthesis[oral]
- Learning Dynamic Relationships for 3D Human Motion Prediction
- Context-Aware Human Motion Prediction
- [Learning a Neural Solver for Multiple Object Tracking]()[oral]
- Skeleton-Based Action Recognition With Shift Graph Convolutional Network
- Semantics-Guided Neural Networks for Efficient Skeleton-Based Human Action Recognition

#### face, hand

- Understanding Human Hands in Contact at Internet Scale
- AvatarMe: Realistically Renderable 3D Facial Reconstruction “In-the-Wild”
- Weakly-Supervised Mesh-Convolutional Hand Reconstruction in the Wild
- Deep Facial Non-Rigid Multi-View Stereo
- Can Facial Pose and Expression Be Separated With Weak Perspective Camera?

#### dataset

- HUMBI: A Large Multiview Dataset of Human Body Expressions
- PANDA: A Gigapixel-Level Human-Centric Video Dataset
- HOnnotate: A Method for 3D Annotation of Hand and Object Poses

<details>
  <summary><b>some interesting works</b></summary>
  <p>

- [End-to-End Camera Calibration for Broadcast Videos]()
- Transferring Dense Pose to Proximal Animal Classes
- Dynamic Graph Message Passing Networks
- Self-Learning Video Rain Streak Removal: When Cyclic Consistency Meets Temporal Correspondence
- Learning to Optimize Non-Rigid Tracking
- SuperGlue: Learning Feature Matching With Graph Neural Networks
- Spatial-Temporal Graph Convolutional Network for Video-Based Person Re-Identification
- Minimal Solutions to Relative Pose Estimation From Two Views Sharing a Common Direction With Unknown Focal Length
  </p>
</details>

### ECCV2020
#### 2D human pose
- [Peeking into occluded joints:A novel framework for crowd pose estimation](https://arxiv.org/pdf/2003.10506.pdf)[[code](https://github.com/opec-gcn/OPEC-GCN)]
- [Differentiable Hierarchical Graph Grouping forMulti-Person Pose Estimation](https://arxiv.org/pdf/2007.11864.pdf)
- [Whole-Body Human Pose Estimation in the Wild]()
- [Self-supervised Keypoint Correspondences for Multi-Person Pose Estimation and Tracking in Videos](https://arxiv.org/pdf/2004.12652.pdf)

#### 3D human pose
- [Contact and Human Dynamics from Monocular Video](https://arxiv.org/pdf/2007.11678.pdf)
- [HDNet: Human Depth Estimation for Multi-Person Camera-Space Localization](https://arxiv.org/abs/2007.08943)
- [HMOR: Hierarchical Multi-person Ordinal Relations for Monocular Multi-Person 3D Pose Estimation]()
- [3D Human Shape and Pose from a Single Low-Resolution Image with Self-Supervised Learning](https://sites.google.com/view/xiangyuxu/3d_eccv20)
- [I2L-MeshNet: Image-to-Lixel PredictionNetwork for Accurate 3D Human Pose andMesh Estimation from a Single RGB Image](https://arxiv.org/pdf/2008.03713.pdf)[[code](https://github.com/mks0601/I2L-MeshNet_RELEASE)]

#### multi-person 3d
- [Unsupervised Cross-Modal Alignment for Multi-Person 3D Pose Estimation](https://arxiv.org/pdf/2008.01388.pdf)


#### multi-view
- [Multi-person 3D Pose Estimation in Crowded Scenes Based on Multi-View Geometry](https://arxiv.org/abs/2007.10986)
- [End-to-End Estimation of Multi-Person 3D Poses from Multiple Cameras](https://arxiv.org/abs/2004.06239)[[code](https://github.com/microsoft/multiperson-pose-estimation-pytorch)]
- [Unsupervised Cross-Modal Alignment forMulti-Person 3D Pose Estimation](https://arxiv.org/pdf/2008.01388.pdf)[[project](https://sites.google.com/view/multiperson3D)]

#### detail human
- [Combining Implicit Function Learning andParametric Models for 3D HumanReconstruction](https://arxiv.org/pdf/2007.11432.pdf)

#### HO
- [Polysemy Deciphering Network for Robust Human-Object InteractionDetection](https://arxiv.org/pdf/2008.02918.pdf)[[code](https://github.com/MuchHair/PD-Net)]

<details>
  <summary><b>Other</b></summary>
  <p>
    
- [Towards Part-aware Monocular 3D Human Pose Estimation: An Architecture Search Approach]()
- [Human Interaction Learning on 3D Skeleton Point Clouds for Video Violence Recognition]()
- [Adaptive Computationally Efficient Network for Monocular 3D Hand Pose Estimation]()
- [Long-term Human Motion Prediction with Scene Context]()
- [Forecasting Human-Object Interaction: Joint Prediction of Motor Attention and Actions in First Person Video]()
- [Appearance Consensus Driven Self-Supervised Human Mesh Recovery]()
- [End-to-end Dynamic Matching Network for Multi-view Multi-person 3d Pose Estimation]()
  </p>
</details>

## Resources
<details>
  <summary><b>Other</b></summary>
  <p>
  
  - [Mixamo](https://www.mixamo.com/#/)
  </p>
</details>


## Contribute
You can contribute to this repor by fork and pull.

You can also see [Awesome Human Pose Estimation](https://github.com/cbsudux/awesome-human-pose-estimation), [awesome-3d-human](https://github.com/lijiaman/awesome-3d-human)
