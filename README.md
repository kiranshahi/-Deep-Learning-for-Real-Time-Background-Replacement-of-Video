### Deep learning for Real Time Background Replacement of Video

#### Abstract: 

Background replacement is one of the most used features in video conferencing applications by many people, perhaps mainly for privacy protection, but also for other purposes such as branding, marketing and promoting professionalism. However, the existing applications in video conference tools have serious limitations. Most applications tend to generate strong artefacts (while there is a slight change in the perspective of the background), or require green screens to avoid such artefacts, which results in an unnatural background or even exposes the original background to other users in the video conference. In this work, we aim to study the relationship between the foreground and background in real-time videos. Three different methods are presented and evaluated, including the baseline U-Net, the lightweight U-Net MobileNet, and the U-Net MobileNet&ConvLSTM models. The above models are trained on public datasets for image segmentation. Experimental results show that both the lightweight U-Net MobileNet and the U-Net MobileNet& ConvLSTM models achieve superior performance as compared to the baseline U-Net model.

#### Result
![Result on Person segmentation dataset.](result/Person-Segmentation/result.jpg)

*Results on the Kaggle Person Segmentation dataset.*

#### How to Cite
```
@article{shahi_background,
  author = {Shahi, Kiran and Li, Yongmin},
  title = {Background Replacement in Video Conferencing},
  doi = {https://doi.org/10.53941/ijndi.2023.100004},
  url = {https://www.sciltp.com/journals/ijndi/issue18-paper256.html},
  journal = {IJNDI}
}
```