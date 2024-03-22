import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import sys
import logging

def analyze_image_file(endpoint,key,file):




    # Acquire the logger for this client library. Use 'azure' to affect both
    # 'azure.core` and `azure.ai.vision.imageanalysis' libraries.
    logger = logging.getLogger("azure")

    # Set the desired logging level. logging.INFO or logging.DEBUG are good options.
    logger.setLevel(logging.INFO)

    # Direct logging output to stdout (the default):
    handler = logging.StreamHandler(stream=sys.stdout)
    # Or direct logging output to a file:
    # handler = logging.FileHandler(filename = 'sample.log')
    logger.addHandler(handler)

    # Optional: change the default logging format. Here we add a timestamp.
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    handler.setFormatter(formatter)
    # [END logging]

    # Set the values of your computer vision endpoint and computer vision key as environment variables:

    # Load image to analyze into a 'bytes' object
    with open(file, "rb") as f:
        image_data = f.read()

    # [START create_client_with_logging]
    # Create an Image Analysis client with none redacted log
    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
        logging_enable=True
    )
    # [END create_client_with_logging]

    # Analyze all visual features from an image stream. This will be a synchronously (blocking) call.
    result = client.analyze(
        image_data=image_data,
        visual_features=[
            VisualFeatures.TAGS,
            VisualFeatures.OBJECTS,
            VisualFeatures.CAPTION,
            VisualFeatures.DENSE_CAPTIONS,
            VisualFeatures.READ,
            VisualFeatures.SMART_CROPS,
            VisualFeatures.PEOPLE,
        ],  # Mandatory. Select one or more visual features to analyze.
        smart_crops_aspect_ratios=[0.9, 1.33],  # Optional. Relevant only if SMART_CROPS was specified above.
        gender_neutral_caption=True,  # Optional. Relevant only if CAPTION or DENSE_CAPTIONS were specified above.
        language="en",  # Optional. Relevant only if TAGS is specified above. See https://aka.ms/cv-languages for supported languages.
        model_version="latest",  # Optional. Analysis model version to use. Defaults to "latest".
    )

    # Print all analysis results to the console
    if result.read is not None:
        return result.read




    print(f" Image height: {result.metadata.height}")
    print(f" Image width: {result.metadata.width}")
    print(f" Model version: {result.model_version}")