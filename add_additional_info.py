import yaml
import os

def merge_site_into_index(chart_dir, index_file):
    index_data = {}
    with open(index_file, 'r') as index:
        index_data = yaml.safe_load(index)

    for chart in index_data['entries']:
        site_file = os.path.join(chart_dir, chart, 'site.yaml')
        if os.path.exists(site_file):
            with open(site_file, 'r') as site:
                site_data = yaml.safe_load(site)
            for version in index_data['entries'][chart]:
                version.update(site_data)

    with open(index_file, 'w') as index:
        yaml.dump(index_data, index, default_flow_style=False)

chart_dir = './charts'  # Adjust this path if necessary
index_file = 'index.yaml'
merge_site_into_index(chart_dir, index_file)
