# Helm Chart Repository

This repository contains Helm charts that can be used to deploy applications. Below, you will find instructions on how to add your own chart to the repository and the requirements it must meet.

## Adding an Application

To deploy your own application to this Helm repository, follow these steps:

1. **Fork the Repository**: Start by forking the Helm repository from here.
2. **Add Your Chart**: Add your chart to the `charts` directory in your forked repository.
3. **Submit a Pull Request**: Create a pull request to merge your chart into the main branch of the Helm repository.
4. **Automated Deployment**: Once the pull request is approved and merged, a GitHub Action will be triggered to deploy your application online.

### Adding Additional Configuration

You can add an additional `site.yaml` file to the directory of your chart. This file should be at the same level as `Chart.yaml`. The `site.yaml` file allows you to provide frontend configurations. Below is an example of a `site.yaml` file:

```yaml
imageUrl: "https://www.nginx.com/wp-content/uploads/2021/08/NGINX-Part-of-F5-horiz-black-type-1.svg"
clusterSettings: 
    kubernetesVersion: "v1.27.3"
    controlPlaneMachineCount: 3
    workerMachineCount: 2
    workerMachinesMemory: 4
    machineCores: 2

afterInstallationManual: |
    # What to do after installing?
    This is some example text.
    - list
    - items
```

## Custer Settings
When configuring clusterSettings in site.yaml, consider the following:

- The Kubernetes version should be either v1.27.3 or v1.24.10. (or other versions provided on CloudNativeLab)
- The number of control plane machines should be 1 or 3.
- The number of worker machines should be 1, 2, or 3.
- The memory for worker machines should be a number between 4 and 16.
- The number of machine cores should be 2, 3, or 4.


## Important Notes
Ensure that the name specified in `Chart.yaml` matches the directory name of the chart. This is necessary for the system to fetch additional information from `site.yaml`.