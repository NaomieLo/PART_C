# ECSE429 - PART B

### Group: 6

### Students

- **Deniz Emre**
  Email: deniz.emre@mail.mcgill.ca
  Student ID: 261029931
- **Naomie Lo**
  Email: naomie.lo@mail.mcgill.ca
  Student ID: 261018690

### Video of Tests Running

#### Performance Test

[Watch performance test video here](https://drive.google.com/file/d/1KmXYsQmA132BbuFMT0AWuFWZCH6-_DgO/view?usp=sharing)

#### Static Analysis

[Watch static analysis test video here](https://drive.google.com/file/d/1SOUsaYedDpKGR9FLof1zvqZF3y8ufXee/view?usp=sharing)

### SonarQube Steps (MAC)

1. **CD into OS Folder**

```bash
   cd ~/Users/naomielo~/Desktop/sonar-scanner-6.2.1.4610-macosx-x64/bin/thingifier-1.5.5
```

2. brew services start sonarqube
3. got to http://localhost:9000 in browsers
4. running a local project explained in report

### Performance Testing

1. Install psutil

```bash
   pip install psutil
```

2. Install requests

```bash
   pip install requests
```

3. Install matplotlib

```bash
   pip install matplotlib
```

4. Install pandas

```bash
   pip install pandas
```

5. Run using the following commands in the Performance_Testing folder to display test results:

```
python performance_test.py
python cpu_memory_analysis.py
```
