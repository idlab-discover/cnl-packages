import yaml
import os
import sys

def merge_site_into_index(charts_dir, index_file_path):
    with open(index_file_path, 'r') as index_file:
        index_data = yaml.safe_load(index_file)

    for chart_name in index_data['entries']:
        site_file_path = os.path.join(charts_dir, chart_name, 'site.yaml')
        
        if os.path.exists(site_file_path):
            with open(site_file_path, 'r') as site_file:
                site_data = yaml.safe_load(site_file)
            
            for version_entry in index_data['entries'][chart_name]:
                try:
                    version_entry.update(site_data[version_entry['version']])
                except KeyError:
                    try:
                        version_entry.update(site_data['default'])
                    except KeyError:
                        pass

    # Write the updated index data back to the index.yaml file
    with open(index_file_path, 'w') as index_file:
        yaml.dump(index_data, index_file, default_flow_style=False)

if __name__ == "__main__":
    # Retrieve the paths from environment variables or script arguments
    charts_dir = os.getenv('CHARTS_DIR', sys.argv[1] if len(sys.argv) > 1 else './charts')
    index_file_path = os.getenv('SITE_FILE', sys.argv[2] if len(sys.argv) > 2 else './site.yaml')

    # Execute the merge function
    merge_site_into_index(charts_dir, index_file_path)
