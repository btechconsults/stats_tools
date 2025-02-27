""" Hypothesis Testing: --- T-test (one-sample, two-sample, paired)
Chi-square test for independence and ANOVA (Analysis of Variance)
-- Outlier Detection:, Z-score method, IQR (Interquartile Range) method
--  Extended File Support: JSON and Excel support for dataset loading """
import Project 
import scipy.stats as stats
from typing import Callable, Dict, Optional

class Project_test(Project):
    def __init__(self, name: str, author: str, course: str, dataset_path: Optional[str] = None):
        self.name = name
        self.author = author
        self.course = course
        self.dataset = None
        self.methods: Dict[str, Callable] = {}

        if dataset_path:
            self.load_dataset(dataset_path)

        self._initialize_statistical_methods()

    def get_summary(self) -> str:
        return f"Project: {self.name}\nAuthor: {self.author}\nCourse: {self.course}\nDataset Loaded: {self.dataset is not None}"

    def load_dataset(self, file_path: str):
        try:
            if file_path.endswith(".csv"):
                self.dataset = pd.read_csv(file_path)
            elif file_path.endswith(".json"):
                self.dataset = pd.read_json(file_path)
            elif file_path.endswith(".xlsx"):
                self.dataset = pd.read_excel(file_path)
            print(f"Dataset loaded successfully from {file_path}")
        except Exception as e:
            print(f"Error loading dataset: {e}")

    def add_method(self, name: str, function: Callable):
        self.methods[name] = function

    def execute_method(self, name: str, *args, **kwargs):
        if name in self.methods:
            return self.methods[name](*args, **kwargs)
        else:
            raise ValueError(f"Method '{name}' not found.")

    def _initialize_statistical_methods(self):
        def t_test_one_sample(column: str, popmean: float):
            return stats.ttest_1samp(self.dataset[column], popmean)

        def t_test_independent(col1: str, col2: str):
            return stats.ttest_ind(self.dataset[col1], self.dataset[col2])

        def t_test_paired(col1: str, col2: str):
            return stats.ttest_rel(self.dataset[col1], self.dataset[col2])

        def chi_square_test(col1: str, col2: str):
            contingency_table = pd.crosstab(self.dataset[col1], self.dataset[col2])
            return stats.chi2_contingency(contingency_table)

        def anova_test(*columns):
            return stats.f_oneway(*(self.dataset[col] for col in columns))

        def z_score_outliers(column: str, threshold: float = 3.0):
            z_scores = np.abs(stats.zscore(self.dataset[column]))
            return self.dataset[z_scores > threshold]

        def iqr_outliers(column: str):
            Q1 = self.dataset[column].quantile(0.25)
            Q3 = self.dataset[column].quantile(0.75)
            IQR = Q3 - Q1
            return self.dataset[(self.dataset[column] < (Q1 - 1.5 * IQR)) | (self.dataset[column] > (Q3 + 1.5 * IQR))]

        self.add_method("t_test_one_sample", t_test_one_sample)
        self.add_method("t_test_independent", t_test_independent)
        self.add_method("t_test_paired", t_test_paired)
        self.add_method("chi_square_test", chi_square_test)
        self.add_method("anova_test", anova_test)
        self.add_method("z_score_outliers", z_score_outliers)
        self.add_method("iqr_outliers", iqr_outliers)

if __name__ == "__main__":
    my_project = Project_test("Stat Analysis", "Tyrone", "Data Science", "data.csv")
    print(my_project.get_summary())
    print("T-Test Result:", my_project.execute_method("t_test_one_sample", "age", 30))
    print("Outliers using IQR:", my_project.execute_method("iqr_outliers", "salary"))
