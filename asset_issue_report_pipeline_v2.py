asset_list = [
    "bg_final_v2.png",
    "character_main.psd",
    "effect_v1.jpg",
    "logo.png",
    "virus.exe",
    "effect_v1.jpg",
    "effect v2.JPG"
]

# asset size database
asset_size = {
    "bg_final_v2.png": 25,
    "character_main.psd": 40,
    "effect_v1.jpg": 10,
    "logo.png": 5
}

def validate_assets(asset_list, asset_dic):
    total_assets = len(asset_list)
    #counter
    assets_processed = 0
    assets_skipped = 0

    #collections for reporting
    unclean_name_assets = []
    heavy_assets = []
    light_assets = []
    missing_info_assets = []
    duplicate_assets = []
    invalid_file_assets = []
    

    seen = set()

    for asset in asset_list:

        # Duplicate check
        if asset in seen:
            print(f"ERROR: Duplicate asset skipped -> {asset}")
            duplicate_assets.append(asset)
            assets_skipped += 1
            continue
        seen.add(asset)

        # File type validation
        if not asset.lower().endswith((".png", ".psd", ".jpg")):
            print(f"ERROR: Invalid file type skipped -> {asset}")
            invalid_file_assets.append(asset)
            assets_skipped += 1
            continue

        # Naming cleanliness 
        if " " in asset or asset != asset.lower():
            print(f"WARNING: Unclean name -> {asset}")
            unclean_name_assets.append(asset)

        
        assets_processed += 1

        # Size check
        if asset in asset_dic:
            size = asset_dic[asset]

            if size > 20:
                print(f"INFO: Processing {asset} | Size: {size} MB | HEAVY")
                heavy_assets.append(asset)
            else:
                print(f"INFO: Processing {asset} | Size: {size} MB | LIGHT")
                light_assets.append(asset)
        else:
            print(f"INFO: Processing {asset} | SIZE INFO MISSING")
            missing_info_assets.append(asset)

    # Asset Validation report
    print("\n------- ASSET VALIDATION REPORT -------")
    print(f"Total assets found: {total_assets}")
    print(f"Assets processed: {assets_processed}")
    print(f"Assets skipped: {assets_skipped}")

    print("\n----- Issues Detected -----")
    print(f"Duplicate assets -{len(duplicate_assets)}: {duplicate_assets}")
    print(f"Invalid file types-{len(invalid_file_assets)}: {invalid_file_assets}")
    print(f"Unclean names-{len(unclean_name_assets)}: {unclean_name_assets}")
    print(f"Missing size info-{len(missing_info_assets)}: {missing_info_assets}")

    print("\n----- Valid Assets -----")
    print(f"Heavy assets-{len(heavy_assets)}: {heavy_assets}")
    print(f"Light assets-{len(light_assets)}: {light_assets}")

validate_assets(asset_list, asset_size)
