# Medical Domain Data

We have provided you with a joint probability distribution of symptons, conditions and diseases based on the "flu" example in class. Certain diseases are more likely than others given certain symptons, and a model such as this can be used to help doctors make a diagnosis.  (Don't actually use this for diagnosis, though!). The ground-truth joint probability distribution consists of twelve binary random variables and contains \( 2^{12} \) possible configurations (numbered 0 to 4095), which is small enough that you can enumerate them exhaustively. The variables are as follows:

* (0) **IsSummer** *true* if it is the summer season, false otherwise.
* (1) **HasFlu** *true* if the patient has the flu.
* (2) **HasFoodPoisoning** *true* if the patient has food poisoning.
* (3) **HasHayFever** *true* if patient has hay fever.
* (4) **HasPneumonia** *true* if the patient has pneumonia.
* (5) **HasRespiratoryProblems** *true* if the patient has problems in the respiratory system.
* (6) **HasGastricProblems** *true* if the patient has problems in the gastro-intestinal system.
* (7) **HasRash** *true* if the patient has a skin rash.
* (8) **Coughs** *true* if the patient has a cough.
* (9) **IsFatigued** *true* if the patient is tired and fatigued.
* (10) **Vomits** *true* if the patient has vomited.
* (11) **HasFever** *true* if the patient has a high fever.

You can download all the data [here](medical_domain_dataset.gz). The archive contains two files:

* **joint.dat**: The true joint probability distribution over the twelve binary variables. Since each variable is binary, we can represent a * full variable assignment as a bitstring. This file lists all 2^12 assignments (one in each line) as pairs "Integer Probability" where "Integer" is an integer encoding of the bitstring. Specifically, assuming false=0 and true=1, an assignment to all variables results in a 12-bit binary number (with the index of the variables shown in parantheses above) which is converted to a decimal number. For example, assignment 0 represents all variables are false, 1 represents only IsSummer is true, 2 represents only HasFlu is true, and so on.
* **dataset.dat**: The dataset consists of samples from the above probability distribution. Each line of the file contains a complete assignment to all the variables, encoded as an integer (as described above).
