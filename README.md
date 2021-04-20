## Gryffin: An algorithm for Bayesian optimization for categorical variables informed by physical intuition with applications to chemistry

Gryffin is an open source algorithm which implements Bayesian optimization for categorical variables and mixed categorical-continuous parameter domains [1]. It follows the learning principles of Phoenics [2]: proposals are evaluated based on a kernel density-based surrogate model that scales linearly with the number of observations.


## Getting started

Gryffin is developed for Linux based systems. Although we hope that you will not encounter any issues we would appreciate if you contacted us should you run into any of them.

To install Gryffin from source you can clone this repository and execute the following steps.

##### From source 

Gryffin can be installed from source. 
```
git clone https://github.com/Atinary-technologies/gryffin
cd gryffin 
pip install .
```

## Running Gryffin

Gryffin identifies optimal parameter choices in a closed-loop approach. Given a set of prior observations, consisting of evaluated parameters and associated measurements, it can recommend several parameter choices for future evaluation.

A basic skeleton of the code to run Gryffin is as follows:
```
from gryffin import Gryffin

##  BUDGET (int): number of evaluations of the black-box function we want to optimize.
##  benchmark (function): 'black box' function that returns the merit obtained for a certain parameter setup.

# create an instance from a configuration file
CONFIG_FILE = 'config.json'
gryffin = Gryffin(CONFIG_FILE)

observations = []
for _ in range(BUDGET):

    # gryffin recommends a number of parameter setups to evaluate based on previous observations
    samples  = gryffin.recommend(observations = observations)
   
    for sample in samples:
        # black box models is queried with the recommended parameter setups 
        measurement   = benchmark(sample)
        sample['obj'] = measurement
        observations.append(sample)
```

## Configuration file

The config file (`config.json`) defines the optimization problem and the setup of Gryffin. It must contain the three following fields: `general`, `parameters` and `objectives`.

- `general`. It contains hyperparameter choices that will affect the performance of Gryffin. The whole list of hyperparameters and their default values are available at `src/gryffin/utilities/defaults.py`. Some of the most important hyperparameters (type) are:
    - `auto_desc_gen` (bool): It enables dynamic Gryffin for the case it is set to `True` and descriptors are provided.
    - `sampling_strategies` (int): Number of acquisition functions as per the Phoenics framework. 

- `parameters`. It characterizes the parameters that are to be optimized. Gryffin supports both continuous, categorical and discrete parameters. Each parameter type is characterized with a number of attributes.

    - **Continuous** parameters are characterized by an upper (`high`) and lower (`low`) bound.
    - **Categorical** parameters take on one of a limited number of possible options. Options may be characterized by descriptors. Both information should be available in `cat_details`.
    - **Discrete** parameters also take on one of a limited number of possible options. Options are in the interval defined by an upper (`high`) and lower (`low`) bound.

- `objectives`. It enumerates the list of objectives to optimize. For the case where the user defines more than one objective, all objectives are aggregated into one single objective based on the Chimera framework [3]. In either case, each objective must always be characterized with:
    - `name` (str): Name of the property to be optimized.
    - `goal` (maximize/minimize).

    Moreover, for multi-objective optimization problems there are additional attributes that must be provided:
    - `hierarchy` (int): hierarchy importance for each individual objective. The lower the more relevant it becomes.
    - `tolerance` (float): relative tolerance value.

For a more detailed description of each hyperparameter, we refer the user to [1], [2] and [3].

Find below an example of config file.
```
{
	"general": {
		"auto_desc_gen": "False",
		"parallel":      "True",
		"boosted":       "False",
		"sampling_strategies": 2
	},
	"parameters": [
			{"name": "param_0", "type": "categorical", "size": 1, "category_details": "CatDetails/cat_details_param_0.pkl"},
			{"name": "param_1", "type": "categorical", "size": 1, "category_details": "CatDetails/cat_details_param_0.pkl"}
	],
	"objectives": [
			{"name": "obj", "goal": "minimize"}
    ]
}
```

## Optimization of analytical functions

The goal of bayesian optimization is to find the parameter setup that maximizes/minimizes a black-box function. For benchmarking purposes, optimization techniques are often evaluated in functions whose analytical form is known. The `benchmark_functions.py` file contains examples of known functions such as Dejong, Camel or Ackley.

*NOTE:* The functions defined in `benchmark_functions.py` expect the suggested samples to be formatted as numpy arrays. 

### References
[1] Häse, F., Roch, L.M. and Aspuru-Guzik, A., 2020. Gryffin: An algorithm for Bayesian optimization for categorical variables informed by physical intuition with applications to chemistry. arXiv preprint arXiv:2003.12127.

[2] Häse, F., Roch, L. M., Kreisbeck, C. and  Aspuru-Guzik, A. Phoenics: A Bayesian Optimizer for Chemistry. ACS Cent. Sci. 4.6 (2018): 1134-1145.

[3] Häse, F., Roch, L. M. and  Aspuru-Guzik, A. Chimera: Enabling hierarchy based multi-objective optimization for self-driving laboratories. Chemical Science 2018, 9(39), 7642-7655.
