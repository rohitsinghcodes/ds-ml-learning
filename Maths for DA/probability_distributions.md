# Probability Distributions

## 1. Introduction
- Probability Distribution: Function showing all possible values of a random variable and their probabilities.  
- Types: Discrete and Continuous distributions.

---

## 2. Uniform Discrete Distribution
- Probability of each outcome:  
  P(X = x) = 1 / n  
- Mean: μ = (n + 1) / 2  
- Variance: σ² = (n² - 1) / 12  

---

## 3. Bernoulli Distribution
- Single trial with success (1) or failure (0)  
- Probability Mass Function (PMF):  
  P(X = x) = p^x * (1-p)^(1-x), x = 0,1  
- Mean: μ = p  
- Variance: σ² = p(1-p)  

---

## 4. Binomial Distribution
- Number of successes in n independent trials  
- PMF:  
  P(X = k) = C(n,k) * p^k * (1-p)^(n-k)  
- Mean: μ = n * p  
- Variance: σ² = n * p * (1-p)  

---

## 5. Poisson Distribution
- Number of events in a fixed interval  
- PMF:  
  P(X = k) = (λ^k * e^(-λ)) / k!  
- Mean: μ = λ  
- Variance: σ² = λ  

---

## 6. Continuous Uniform Distribution
- Probability Density Function (PDF):  
  f(x) = 1 / (b - a), a ≤ x ≤ b  
- Mean: μ = (a + b) / 2  
- Variance: σ² = (b - a)² / 12  

---

## 7. Exponential Distribution
- Time between events in a Poisson process  
- PDF:  
  f(x) = λ * e^(-λx), x ≥ 0  
- Mean: μ = 1 / λ  
- Variance: σ² = 1 / λ²  

---

## 8. Normal Distribution
- PDF:  
  f(x) = (1 / (σ√2π)) * e^(-(x-μ)² / (2σ²))  
- Mean: μ  
- Variance: σ²  

---

## 9. Standard Normal Distribution (SND)
- Z = (X - μ) / σ  
- Mean: 0, Variance: 1  

---

## 10. Normalization
- Convert X to Z-score:  
  Z = (X - μ) / σ  

---

## 11. T-Distribution
- Used when population standard deviation σ is unknown and sample size is small  
- Test statistic:  
  t = (x̄ - μ) / (s / √n)  
- Mean: 0, Variance: n / (n-2) for n > 2  
