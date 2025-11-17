# Dataset Bias in Fake News Detection: Why 99% Accuracy Doesn't Mean What You Think

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange.svg)](https://scikit-learn.org/)
[![Transformers](https://img.shields.io/badge/Transformers-4.44.0-green.svg)](https://huggingface.co/transformers/)

## 📋 Overview

This research exposes systematic bias in popular fake news detection datasets. Our analysis reveals that **94-100% accuracy scores** commonly reported in literature are misleading artifacts of flawed dataset construction—models learn to recognize writing styles and sources rather than detect actual misinformation.

### Key Findings
- ✅ All models (Naive Bayes to BERT) achieved 94-100% accuracy across three datasets
- ✅ Models learned source recognition (e.g., "reuters" = real news) not fact-checking
- ✅ Perfect 100% accuracy on synthetic dataset = trivially easy task
- ✅ Dataset bias is **systematic and universal**, not dataset-specific

---

## 📊 Datasets Analyzed

| Dataset | Size | Distribution | Purpose |
|---------|------|--------------|---------|
| **Large Kaggle** | 44,898 articles | 23,481 fake / 21,417 real | Most popular benchmark |
| **Balanced** | 9,900 articles | 5,000 fake / 4,900 real | Test if balance reduces bias |
| **Synthetic** | 1,000 articles | 468 fake / 532 real | Test with obvious examples |

**Source:** [Kaggle Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

---

## 🤖 Models Evaluated

**Traditional ML:** Naive Bayes, Logistic Regression, Decision Tree, Random Forest, SVM  
**Deep Learning:** BERT (bert-base-uncased)  
**Feature Extraction:** TF-IDF (8,000 features, unigrams + bigrams)

---

## 📈 Results

### Model Performance Across Datasets

| Model | Dataset 1 (44K) | Dataset 2 (9.9K) | Dataset 3 (1K) |
|-------|-----------------|------------------|----------------|
| Naive Bayes | 94.27% | 96.62% | **100%** |
| Logistic Regression | 98.83% | 99.04% | **100%** |
| Decision Tree | 99.48% | 99.70% | **100%** |
| Random Forest | **99.73%** | **99.95%** | **100%** |
| SVM | 99.57% | 99.70% | **100%** |
| BERT | 92.75% | ~99% | **100%** |

### What Models Actually Learned

**Fake News Markers:**
- Political terms: "moscow", "russian", "minister"
- Sensational language
- Blog-style writing

**Real News Markers:**
- Source attribution: **"reuters"** (smoking gun!)
- Formal journalistic style: "via", "told", "according to"
- Quantitative precision: "percent", "data"

**Critical Finding:** Subject category alone = 100% classification accuracy on Dataset 1!
- "politicsNews" & "worldnews" → ALL REAL
- "News" & "politics" & "left-news" → ALL FAKE

---

## 💡 Key Insights

### The Problem
```
Models Don't Detect Lies → They Recognize Reuters Style
99% Accuracy ≠ Fake News Detection
```

**What This Means:**
- ❌ Current benchmarks test **source identification**, not misinformation detection
- ❌ Sophisticated fake news mimicking journalism style would evade detection
- ❌ Deployed systems trained on these datasets will **fail in production**
- ❌ The real problem remains **unsolved**

### Why Perfect Accuracy is Bad
Perfect scores indicate the task is **trivially easy**—models exploit superficial patterns:
1. Word presence ("reuters" = real)
2. Writing style (formal = real, sensational = fake)
3. Metadata (subject category = perfect predictor)

---

## 🔮 Future Work

### Immediate Priorities
- 🎯 Build adversarial test sets (rewrite fake news in Reuters style)
- 🎯 Cross-dataset evaluation (train on A, test on B)
- 🎯 Claim-level detection (verify specific facts, not entire articles)

### Long-term Vision
- Multi-modal detection (text + images + videos)
- Real-world deployment testing with fact-checkers
- Human-AI collaborative systems
- Better benchmark datasets with controlled confounds

---

## 🛠️ Installation
```bash
# Clone repository
git clone https://github.com/yourusername/fake-news-bias-analysis.git
cd fake-news-bias-analysis

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

### Requirements
```
pandas
numpy
scikit-learn==1.3.0
nltk
matplotlib
seaborn
transformers==4.44.0
torch
datasets
```

---

## 🚀 Usage
```bash
# Run analysis on different datasets
python models/naive_bayes_logistic_svm_rf_dt_based_detector.py  # Dataset 1
python models/balanced_dataset_detector.py                       # Dataset 2
python models/synthetic_dataset_detector.py                      # Dataset 3
python models/bert_detector.py                                   # BERT fine-tuning
```

Results and visualizations are saved in `results/` directory.

---

## 📁 Repository Structure
```
├── data/                       # Datasets (Fake.csv, True.csv, etc.)
├── models/                     # Training scripts
├── analysis/                   # Lexical analysis and visualizations
├── results/                    # Generated figures and metrics
├── paper/                      # IEEE conference paper (PDF)
├── presentation/               # Project slides
└── requirements.txt
```

---

## 📚 Citation

If you use this work, please cite:
```bibtex
@inproceedings{vaidya2025datasetbias,
  title={Dataset Bias in Fake News Detection: Why 99\% Accuracy Doesn't Mean What You Think},
  author={Vaidya, Siddhi and Thakur, Shruti},
  booktitle={[Conference Name]},
  year={2025}
}
```

---

## 👥 Authors

**Siddhi Vaidya** • **Shruti Thakur**

---

## ⚠️ Important Disclaimer

**High benchmark accuracy ≠ Real-world effectiveness**

This research demonstrates that 99% accuracy on popular datasets does NOT mean the model can detect real-world misinformation. Practitioners should:

1. **NOT deploy** systems trained solely on these datasets
2. **Test extensively** on adversarial examples
3. **Include human oversight** in production systems
4. **Remain skeptical** of benchmark-only evaluation

---

## 🤝 Contributing

We welcome:
- 🐛 Bug reports and issues
- 💡 Ideas for better evaluation methods
- 🤝 Collaborations on benchmark construction
- 📊 Additional dataset analyses

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) for the dataset
- Hugging Face for Transformers library
- scikit-learn and NLTK communities

---

<div align="center">

**"The first step in solving a problem is recognizing there is one."**

*Let's build better benchmarks together.* 🚀

⭐ Star this repo if you find it useful! ⭐

</div>
