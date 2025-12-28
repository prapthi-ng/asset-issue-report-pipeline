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

    valid_assets = 0
    unclean_name = 0
    heavy = 0
    light = 0
    missing_info = 0
    duplicate = 0
    invalid_file_type = 0
    assets_processed = 0
    assets_skipped = 0

    seen = set()

    for asset in asset_list:

        # Duplicate check
        if asset in seen:
            print(f"ERROR: Duplicate asset skipped -> {asset}")
            duplicate += 1
            assets_skipped += 1
            continue
        seen.add(asset)

        # File type validation
        if not asset.lower().endswith((".png", ".psd", ".jpg")):
            print(f"ERROR: Invalid file type skipped -> {asset}")
            invalid_file_type += 1
            assets_skipped += 1
            continue

        # Naming cleanliness 
        if " " in asset or asset != asset.lower():
            print(f"WARNING: Unclean name -> {asset}")
            unclean_name += 1

        valid_assets += 1
        assets_processed += 1

        # Size check
        if asset in asset_dic:
            size = asset_dic[asset]

            if size > 20:
                heavy += 1
                print(f"INFO: Processing {asset} | Size: {size} MB | HEAVY")
            else:
                light += 1
                print(f"INFO: Processing {asset} | Size: {size} MB | LIGHT")
        else:
            missing_info += 1
            print(f"INFO: Processing {asset} | SIZE INFO MISSING")

    # Asset Validation report
    print("\n------- ASSET VALIDATION REPORT -------")
    print(f"Total assets checked : {total_assets}")
    print(f"Assets processed     : {assets_processed}")
    print(f"Assets skipped       : {assets_skipped}")

    print("\n----- Valid Assets -----")
    print(f"Valid file types     : {valid_assets}")
    print(f"Heavy assets         : {heavy}")
    print(f"Light assets         : {light}")

    print("\n----- Issues Detected -----")
    print(f"Duplicate assets     : {duplicate}")
    print(f"Invalid file types   : {invalid_file_type}")
    print(f"Unclean names        : {unclean_name}")
    print(f"Missing size info    : {missing_info}")

validate_assets(asset_list, asset_size)
