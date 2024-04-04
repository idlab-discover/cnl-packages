'''
This script will add a new version to the site.yaml if there is a new version inside the index.yaml
and will copy the site.yaml from the chart to the corresponding new verison inside 
the site.yaml in the root directory.
'''

import yaml
import os
import sys

def update_site_with_new_version(charts_dir, index_file_path, site_file_path):
    with open(index_file_path, 'r') as index_file:
        index_data = yaml.safe_load(index_file)

    if os.path.exists(site_file_path):
        with open(site_file_path, 'r') as site_file:
            site_data = yaml.safe_load(site_file) or {'entries': {}}
    else:
        site_data = {'entries': {}}

    for chart_name, versions in index_data['entries'].items():
        for version_info in versions:
            version = version_info['version']
            print(f"Processing {chart_name}-{version}")
            application_site_file_path = os.path.join(charts_dir, chart_name, 'site.yaml')
            if os.path.exists(application_site_file_path):
                with open(application_site_file_path, 'r') as app_site_file:
                    app_site_data = yaml.safe_load(app_site_file)
                    
                    if chart_name not in site_data['entries']:
                        site_data['entries'][chart_name] = {}
                    
                    if version not in site_data['entries'][chart_name]:
                        site_data['entries'][chart_name][version] = app_site_data
                
    with open(site_file_path, 'w') as site_file:
        yaml.dump(site_data, site_file, default_flow_style=False)

if __name__ == "__main__":
    charts_dir = os.getenv('CHARTS_DIR', sys.argv[1] if len(sys.argv) > 1 else './charts')
    index_file_path = os.getenv('INDEX_FILE', sys.argv[2] if len(sys.argv) > 2 else './index.yaml')
    site_file_path = os.getenv('SITE_FILE', sys.argv[3] if len(sys.argv) > 3 else './site.yaml')

    update_site_with_new_version(charts_dir, index_file_path, site_file_path)
