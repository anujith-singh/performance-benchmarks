## ⚡ Python Performance Benchmarks

> *“Don’t assume. Measure.”*  
>
> I’m a performance junkie — I like testing how small code choices impact execution time at scale.

Currently includes a benchmark comparing:
- `for` vs `enumerate` vs `range(len())`

More benchmarks coming soon 🚀

---

### 🚀 Run a benchmark
```bash
git clone git@github.com:anujith-singh/performance-benchmarks.git
cd performance-benchmarks
pipenv install
pipenv run python loops/loop_performance_benchmark.py
```

Each script prints timing data and shows a performance chart.

---

### 🧩 Philosophy
> Optimize only when it matters.  
> When it does — measure, don’t assume.

