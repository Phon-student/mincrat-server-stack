import os
import anvil

def scan_region_files(world_path):
    region_dir = os.path.join(world_path, "region")
    if not os.path.exists(region_dir):
        print(f"No region folder found at {region_dir}")
        return

    print(f"Scanning region files in {region_dir}...\n")
    for filename in os.listdir(region_dir):
        if filename.endswith(".mca"):
            file_path = os.path.join(region_dir, filename)
            try:
                region = anvil.Region.from_file(file_path)
                for x in range(32):
                    for z in range(32):
                        if region.chunk_location(x, z):
                            try:
                                region.get_chunk(x, z)
                            except Exception as e:
                                print(f"❌ Corrupt chunk at {filename} ({x}, {z}): {e}")
                print(f"✅ Checked {filename}")
            except Exception as e:
                print(f"❌ Failed to open {filename}: {e}")

# Change this path to your world folder
world_folder_path = "data/world/region"
scan_region_files(world_folder_path)
