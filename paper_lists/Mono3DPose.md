## Monocular 3D Pose and Shape Estimation of Multiple People in Natural Scenes 

### 论文目标

 一个视觉感知系统.可以对互动中的每个人进行动作识别.

* 推断2d和3d动作,从模型和图片级别的语义表示取识别单图里的多人的动作.
* 自动整合场景约束,包括地平面参照和多人同时占用的空间约束
* 通过优化解决时间人员分配问题,并考虑关联时间的姿态和运动重建,同时保持图像对准保真度,将单幅图像模型扩展为视频

### 论文成果

* 提出了一个融合了2d人体关节检测, 语义分割和3d 动作识别的feedforwar-feedback模块, 该模块使用了一个新的语义cost函数, 使模型的主体部分和它们对应的语义图片区域对齐,并考虑了估计的不确定性.
* 场景一致性测量包括自动估计和整合地平面约束, 以及适应性地避免几个人同时占用相同空间的约束
* 时间人分配问题,基于身体形状,外观和使用Hungarian匹配方法的运动提示,然后求解2d投影和3d时间下的联合多人平滑问题,构成时间流动性约束

### 模型构建

为不失一般性, 考虑有$N_p$ 个人体, $N_f$ 帧视频, 我们的目标函数是,推断最佳的状态变量
$$
\Theta = [\theta^f_p] \in \mathbb{R}^{N_p\times N_f\times 72}\\
\Beta = [\beta^f_p] \in \mathbb{R}^{N_p\times N_f\times 10}\\
T =  [t^f_p] \in \mathbb{R}^{N_p\times N_f\times 3}\\
$$
从单帧的以单人为中心的场景开始构建目标函数$L_I^{p,f}(\Beta,\Theta,T)$
$$
L_I^{p,f} = L_S^{p,f} + L_G^{p,f} + L_R^{p,f} + \sum_{p'=1,p'\neq p}^{N_p}L_C^f(p,p')
$$

### 模型基本过程

1. 输入图片视频
2. 单个Feedforward-Feedback模型,向前输入人的检测\身体部位的标签,和3d动作的初始化结果
3. 2d和3d的动作和形状的假设
4. 在约束下进行多人联合的优化,约束指的是地平面假设,相互位置空间的非相交,图像对齐, 时间分配
5. 多人的3d动作和形状重建



### Feedforward Prediction

定义cost function然后infer最优的参数,一般都是使用欧氏距离,然后,由于1)由DMHS预测的不一定是有效的人体shape,2)两个参数并不一定能正确表示pose,如果添加一些额外的惩罚在参数上的话,可能会出现其他不好的bias.

因此这篇文章提出了3d orientation of limbs.函数惩罚余弦距离, 选择的是两个模型中共享的joint.

实践中发现收敛效果相当好,通常可以收敛到0.但是shape信息丢失了.然后分两步来优化pose和shape.

