# Introduction to Reproducible Model Workflows

### Data aspects
* How will the Data pipeline need to work in production to support an optimized ML
pipeline?
* Where will the ML model run in production?
    * Is it in the cloud, or in an edge device for example?
    
* How will data be acquired and secured for different production environments, and will
data collection constraints impact your ML design?
  
* Will your ML model run on raw and unstructured data, or does it require data
preparation and certain data quality levels?
  * If so, how will data preparation be addressed in an operational setting?
  * Does that constrain the choice of target environment, ML modelling technique used
    or similar? 
  * Do you own and have access to the data needed to train your ML model and run it in
    production?
    * if the access is limited, how does that potentially ML techniques used?
    * For example, do you need dummy data for initial training in the lab, and then
    deploy and run your models using Federated Learning? (distributed ML)
      
/ Data quality
* How are you approaching needed data quality in your ML pipeline
* How will data management be handled in an operational setting
* What are the mandatory quality operational requirements that the Data Engineer 
must know early?
* How will you avoid bias when selecting your training data set? 

/ Monitoring
* Considering the needs of monitoring while in production at the start of the
ML model development will impact development choices and priorities.
  
/ Retraining
* Be sure to consider how you plan to re-train your models once they are in production.
* Remember that even the best models will need to be re-trained because of changing
needs, priorities or other changing preferences. 
  
In this class you will learn how to:

1. Create a clean, organized, reproducible, end-to-end machine learning pipeline 
   from scratch
2. Transform, validate and verify your data (avoid “garbage in, garbage out”)
3. Run experiments, track data, code, and results
4. Select the best performing model and promote it to production
5. Create an artifact ready for deployment, and release your final pipeline

# What is MLops?

A set of best practices and methods for an efficients end-to-end development and 
operation of performant, scalable, reliable, automated and reproducible ML solutions
in a real production setting

# Why reproducible workflow are important
![workflow](https://video.udacity-data.com/topher/2021/May/60b1e1db_real-ml-workflow/real-ml-workflow.png)

# What is a Machine Learning Pipeline

It is a sequence of independent, modular, and reusable components. It can be represented
as a Direct Acyclic Graph (DAG).

An Machine Learning pipeline is made of:

* Components (or steps): independent, reusable and modular pieces of software that 
receive one or more inputs and produce one or more output.
They can be scripts, notebooks or other executables.
* Artifacts: the product of components. They can become the inputs of one or
more subsequent components, thereby linking together the steps of the pipeline. 
Artifacts must be tracked and versioned.

![mlpipeline](https://video.udacity-data.com/topher/2021/June/60b87452_etl-pipeline/etl-pipeline.png)

### Levels of MLOps

#### Level 0
* Monolithic code
* the target is a model and not a ML pipeline
* Limited concern for production during development
* No monitoring in production

Situations:
* Side projects
* Studying new techniques
* Kaggle competitions
* Proof of concepts

#### Level 1
* The development target is the pipeline
* Reusable components
* Code, artifact and experiment tracking
* Easy retrain
* Development/production symmetry
* Monitoring in production

Key enhancements
* Process standardization
* Rapid prototyping
* Fast go-to market
* Avoid model drift
* Learn in production
* Easy handover

#### Level 2
* The development targets are the pipelines components
* Continuous integration: Every change in the components that passes the test is merged
automatically
* Continuous deployment: Every change in the components that passes the test is 
released in the production pipeline
* Continuous training: Every time the pipeline changes or new data arrives the pipeline
is automatically triggered, and a new model is released
  
Key enhancements
* Rapid iteration on prod pipelines
* A/B testing
* Large team working on the same pipelines
* Customers see continuous improvements 

![mlops_levels](https://video.udacity-data.com/topher/2021/May/60b422b8_level-comparison/level-comparison.png)

# Versioning Data and Artifacts

`Runs`: Basic unit of tracking. Typically, one run = one script or notebook execution,
but multiple runs per script are possible.

You can attach to it: 
* parameters
* metrics
* artifacts
* images/plots

`Experiment`: A group of runs constituting one experiment. For example, one execution 
of an entire pipeline made of multiple jobs (runs).

`Project`: A high-level grouping of runs. In the W&B UI you can only look at one project
at the time. You can use one project for development, and a separate production 
project with much more limited development. 

`Artifact`: any file or directory produced by our code during a run.
Every artifact that is logged to a run is automatically versioned by W&B.
For example, if two runs produce an artifact with the same name 
(say a file named model.h5) but the content of the file is different, W&B 
will generate two versions (for example v1 and v2). On the contrary, if two 
runs produce the exact same file (same name and same content), W&B will recognize 
this and will NOT generate a new version.
