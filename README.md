# certora_assemble

## Verification Guide
This project uses Certora for formal verification. Follow these steps to prove the contract logic.

### 1. Activate Environment
Before running any commands, you must activate the Python virtual environment where Certora is installed:
```javascript
source certora-env/bin/activate
```
Note: You should see (certora-env) appear in your terminal prompt.

### 2. Run Verification
You can run the Prover directly from the CLI or using the provided configuration file.

Option A: Using the Config File (Recommended)

```javascript
certoraRun confs/counter.conf
```
Option B: Direct CLI Command

```javascript
certoraRun contracts/Counter.sol --verify Counter:specs/counter.spec
```
### 3. View Results
Once the command is executed:

The CLI will check your Solidity and CVL for errors.
~
It will provide a link to the Certora Dashboard.

Open the link to see the mathematical proof of your assert and satisfy rules.

