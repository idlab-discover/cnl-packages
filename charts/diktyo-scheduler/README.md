# Diktyo as a second scheduler in a K8s cluster

## Table of Contents

<!-- toc -->
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installing the chart](#installing-the-chart)
    - [Install chart using Helm v3.0+](#install-chart-using-helm-v30)
    - [Verify that scheduler and plugin-controller pod are running properly.](#verify-that-scheduler-and-plugin-controller-pod-are-running-properly)
  - [Configuration](#configuration)
<!-- /toc -->

## Installation

Quick start instructions for the setup and configuration of diktyo-as-a-second-scheduler using Helm.

### Prerequisites

- [Helm](https://helm.sh/docs/intro/quickstart/#install-helm)

### Installing the chart

#### Install chart using Helm v3.0+

```bash
$ git clone git@github.com:kubernetes-sigs/scheduler-plugins.git
$ cd charts/
$ helm install diktyo as-a-second-scheduler/ --create-namespace --namespace diktyo
```

#### Verify that scheduler and plugin-controller pod are running properly.

```bash
$ kubectl get deploy -n diktyo
NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
appgroup-controller            1/1     1            1           22s
diktyo-scheduler               1/1     1            1           22s
networktopology-controller     1/1     1            1           22s
scheduler-plugins-controller   1/1     1            1           22s
```

### Configuration

The following table lists the configurable parameters of the as-a-second-scheduler chart and their default values.

| Parameter                                | Description                            | Default                                                    |
|------------------------------------------|----------------------------------------|------------------------------------------------------------|
| `scheduler.name`                         | Scheduler name                         | `diktyo-scheduler`                                         |
| `scheduler.image`                        | Scheduler image                        | `registry.k8s.io/scheduler-plugins/kube-scheduler:v0.26.7` |
| `scheduler.leaderElect`                  | Scheduler leaderElection               | `false`                                                    |
| `scheduler.weight`                       | Scheduler Weight (Score plugin)        | `5`                                                        |
| `scheduler.replicaCount`                 | Scheduler replicaCount                 | `1`                                                        |
| `controller.name`                        | Controller name                        | `scheduler-plugins-controller`                             |
| `controller.image`                       | Controller image                       | `registry.k8s.io/scheduler-plugins/controller:v0.26.7`     |
| `controller.replicaCount`                | Controller replicaCount                | `1`                                                        |
| `appGroupController.name`                | appGroupController name                | `appgroup-controller`                                      |
| `appGroupController.image`               | appGroupController image               | `jpedro1992/appgroup-controller:v1.0.3-alpha`              |
| `appGroupController.replicaCount`        | appGroupController replicaCount        | `1`                                                        |
| `networkTopologyController.name`         | networkTopologyController name         | `networktopology-controller`                               |
| `networkTopologyController.image`        | networkTopologyController image        | `jpedro1992/networktopology-controller:v1.0.3-alpha`       |
| `networkTopologyController.replicaCount` | networkTopologyController replicaCount | `1`                                                        |
| `plugins.namespaces`                     | Plugins namespaces by default          | `["default"]`                                              |
| `plugins.weightsName`                    | Plugins weightsName by default         | `"NetperfCosts"`                                           |
| `plugins.networkTopologyName`            | Plugins networkTopologyName by default | `"nt-cluster"`                                             |