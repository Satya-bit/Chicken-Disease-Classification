# Chicken-Disease-Classification
## Aim

Here the aim of the prject is to determine that form the image uploaded by the user whether the disease is having Coccidiosis or is it healthy?

## Workflow

1. Update config.yaml
2. Update secrets.yaml [Optional] - Suppose if database is there and if there are some secret key then use this file
3. Update params.yaml
4. Update the entity - Basically it is the return type of the function
5. Update the configuration manager in src config
6. Update the components- Here data ingestion, base model preparation callbacks, model trainer, model evaluation will be created 
7. Update the pipeline
8. Update the main.py
9. Upate the dvc.yaml - To track pipelines

-> For fronted I have used HTML, CSS with Flask as a framework.

-> VGG-16 CNN model is used for prediction.
## Final results

->As per the below image you can see that my model was able to predict that the fecal image was of Healthy chicken
![image](https://github.com/user-attachments/assets/0d0ba6de-4e0c-4171-9cb9-0d8b496a35cc)

->As per the below image you can see that my model was able to predict that the fecal image was of Coccidiosis chicken
![image](https://github.com/user-attachments/assets/76637d96-678b-42ec-a04d-7b64a142856c)

