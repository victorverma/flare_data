import os
import urllib.request

# The files below were found by following links from https://www.ngdc.noaa.gov/stp/satellite/goes-r.html. The links to follow are those for the
# "Flare Summary" product of the XRS instrument. Links may change over time as files are updated or reorganized.
urls = {
    "goes13": "https://www.ncei.noaa.gov/data/goes-space-environment-monitor/access/science/xrs/goes13/xrsf-l2-flsum_science/sci_xrsf-l2-flsum_g13_s20130607_e20171214_v2-3-0.nc",
    "goes14": "https://www.ncei.noaa.gov/data/goes-space-environment-monitor/access/science/xrs/goes14/xrsf-l2-flsum_science/sci_xrsf-l2-flsum_g14_s20090919_e20200304_v2-3-0.nc",
    "goes15": "https://www.ncei.noaa.gov/data/goes-space-environment-monitor/access/science/xrs/goes15/xrsf-l2-flsum_science/sci_xrsf-l2-flsum_g15_s20100407_e20200304_v2-3-0.nc",
    "goes16": "https://data.ngdc.noaa.gov/platforms/solar-space-observing-satellites/goes/goes16/l2/data/xrsf-l2-flsum_science/sci_xrsf-l2-flsum_g16_s20170209_e20241122_v2-2-0.nc",
    "goes17": "https://data.ngdc.noaa.gov/platforms/solar-space-observing-satellites/goes/goes17/l2/data/xrsf-l2-flsum_science/sci_xrsf-l2-flsum_g17_s20180601_e20230110_v2-2-0.nc",
    "goes18": "https://data.ngdc.noaa.gov/platforms/solar-space-observing-satellites/goes/goes18/l2/data/xrsf-l2-flsum_science/sci_xrsf-l2-flsum_g18_s20220905_e20241122_v2-2-0.nc"
}

output_dir = "../data/raw"
for key, url in urls.items():
    file_path = os.path.join(output_dir, f"{key}.nc")
    print(f"Downloading {key} data from {url}...")
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"Saved to {file_path}")
    except Exception as e:
        print(f"Failed to download {key} data: {e}")
