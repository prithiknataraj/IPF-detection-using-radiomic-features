import radiomics
from radiomics import featureextractor
import SimpleITK as sitk

# Load the image and mask
image_path = "path/to/image.nii"  # or .dcm if using DICOM
mask_path = "path/to/mask.nii"  # or .dcm if using DICOM

image = sitk.ReadImage(image_path)
mask = sitk.ReadImage(mask_path)

# Initialize the extractor with default parameters
extractor = featureextractor.RadiomicsFeatureExtractor()

# Extract features
features = extractor.execute(image, mask)

# Print extracted features
for feature_name, feature_value in features.items():
    print(f"{feature_name}: {feature_value}")