import os
import cv2
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

# Define input directories
original_images_dir = "/home/dhiren/Agisoft_Dataset"
rendered_images_dir = "/home/dhiren/gaussian-splatting/output/551368e8-e/test/ours_30000/renders"

# Collect sorted lists of PNG files
original_files = sorted([f for f in os.listdir(original_images_dir) if f.endswith(".png")])
rendered_files = sorted([f for f in os.listdir(rendered_images_dir) if f.endswith(".png")])

# Initialize results table
results = []

# Compare each pair of original and rendered images
for orig_name, rend_name in zip(original_files, rendered_files):
    orig_path = os.path.join(original_images_dir, orig_name)
    rend_path = os.path.join(rendered_images_dir, rend_name)

    original_img = cv2.imread(orig_path)
    rendered_img = cv2.imread(rend_path)

    if original_img is None or rendered_img is None:
        continue

    # Resize original to match rendered dimensions
    original_img = cv2.resize(original_img, (rendered_img.shape[1], rendered_img.shape[0]))

    # Compute PSNR and SSIM
    psnr_value = peak_signal_noise_ratio(original_img, rendered_img, data_range=255)
    ssim_value = structural_similarity(original_img, rendered_img, channel_axis=2)

    # Store results
    results.append((orig_name, rend_name, round(psnr_value, 2), round(ssim_value, 4)))

# Display results
print("Original\tRendered\tPSNR\tSSIM")
for row in results:
    print("\t".join(map(str, row)))
