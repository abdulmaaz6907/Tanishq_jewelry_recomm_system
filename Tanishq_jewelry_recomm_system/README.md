---
title: Tanishq Jewelry Recomm System
emoji: 💍✨💎✨
colorFrom: pink
colorTo: pink
sdk: gradio
sdk_version: 5.25.2
app_file: app.py
pinned: true
license: apache-2.0
short_description: upload and get 💯💎accurate tanishq jewlery recommendation
---




---
#### project work flow and pipelining:

```markdown
app.py  -->   frontend/gradio_app.py  
  |  
  |  
  ├──> frontend/input_handlers.py  
  |       |  
  |       |  
  |       ├──> backend/jewelry_recomm_service.py  
  |       |      |  
  |       |      |  
  |       |      ├──> backend/supportingfiles/model_loader.py  
  |       |      |      ├──> config.py  (INDEX_PATH, METADATA_PATH, DEVICE)  
  |       |      |  
  |       |      |  
  |       |      ├──> backend/supportingfiles/image_processor.py  
  |       |      |      ├──> config.py  (get_image_transform, DEVICE)  
  |       |      |  
  |       |      |    
  |       |      ├──> backend/supportingfiles/recommender.py  
  |       |             ├──> config.py  (DEFAULT_NUM_RECOMMENDATIONS)  
  |       |  
  |       |  
  |       ├──> utils/formatter.py  (Formats output)  
  | 
  |  
  |  
  └──> config.py  (Standalone configuration file)  

--------------------------------------------------------------------------------------------------------------