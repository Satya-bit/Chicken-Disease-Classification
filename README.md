# Chicken-Disease-Classification

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