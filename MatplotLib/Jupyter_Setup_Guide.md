# 📓 Jupyter Notebook Setup Guide for Kiro

## ✅ Step-by-Step Instructions

### **1. Install Jupyter Extension**
You've already done this! ✓

### **2. Install Jupyter in Your Python Environment**

Open your terminal in Kiro and run:

```bash
pip install jupyter notebook ipykernel
```

Or if you're using Python 3 specifically:

```bash
pip3 install jupyter notebook ipykernel
```

### **3. Verify Installation**

Check if Jupyter is installed:

```bash
jupyter --version
```

You should see version numbers for jupyter core, notebook, etc.

### **4. Open a Jupyter Notebook**

**Method 1: Create New Notebook**
1. Right-click in the file explorer
2. Select "New File"
3. Name it with `.ipynb` extension (e.g., `my_notebook.ipynb`)
4. Kiro will automatically open it in Jupyter mode

**Method 2: Open Existing Notebook**
1. Click on any `.ipynb` file in your workspace
2. It will open in the Jupyter notebook interface

### **5. Select Python Kernel**

When you open a notebook:
1. Look for "Select Kernel" button at the top right
2. Click it and choose your Python interpreter
3. If you don't see it, select "Python Environments" and pick one

### **6. Run Cells**

- **Run single cell**: Click the ▶️ play button next to the cell, or press `Shift + Enter`
- **Run all cells**: Use the "Run All" button in the toolbar
- **Add new cell**: Click the `+ Code` or `+ Markdown` buttons

---

## 🎯 Quick Test

I've created a test notebook for you: `test_notebook.ipynb`

**To test it:**
1. Open `test_notebook.ipynb` in Kiro
2. Select your Python kernel (top right)
3. Click "Run All" or run each cell individually
4. You should see plots appear below the code cells

---

## 🔧 Troubleshooting

### **Problem: "No Kernel" or "Kernel Not Found"**
**Solution:**
```bash
python -m ipykernel install --user
```

### **Problem: Matplotlib plots not showing**
**Solution:** Make sure you have matplotlib installed:
```bash
pip install matplotlib
```

### **Problem: Extension not working**
**Solution:**
1. Restart Kiro
2. Check if the Jupyter extension is enabled in Extensions panel
3. Try reinstalling: Search for "Jupyter" in Extensions and reinstall

### **Problem: Can't find Python interpreter**
**Solution:**
1. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac)
2. Type "Python: Select Interpreter"
3. Choose your Python installation

---

## 💡 Pro Tips

### **Keyboard Shortcuts:**
- `Shift + Enter` - Run cell and move to next
- `Ctrl + Enter` - Run cell and stay
- `A` - Add cell above (in command mode)
- `B` - Add cell below (in command mode)
- `DD` - Delete cell (in command mode)
- `M` - Change to Markdown cell
- `Y` - Change to Code cell

### **Best Practices:**
1. **Save frequently** - Use `Ctrl + S`
2. **Restart kernel** if things get weird - "Restart" button in toolbar
3. **Clear outputs** before committing to Git - keeps files small
4. **Use markdown cells** for documentation and explanations

---

## 📚 Example Notebook Structure

```python
# Cell 1: Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cell 2: Load Data
df = pd.read_csv('data.csv')
df.head()

# Cell 3: Data Analysis
df.describe()

# Cell 4: Visualization
plt.plot(df['x'], df['y'])
plt.show()
```

---

## 🎨 Using Matplotlib in Jupyter

Matplotlib works great in Jupyter! Plots appear directly below code cells.

**Example:**
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.show()  # Plot appears below!
```

---

## 🚀 Next Steps

1. ✅ Open `test_notebook.ipynb` and run it
2. ✅ Create your own notebook for matplotlib practice
3. ✅ Try the examples from the Readme.md in a notebook
4. ✅ Experiment with different plot types

**Happy Coding! 🎉**
