# Certora Formal Verification

A professional starter guide for using **Certora Prover** to formally verify Solidity smart contracts.

This repository demonstrates how to:

* Set up the Certora environment
* Run formal verification on smart contracts
* Interpret verification results from the Certora Dashboard

---

# What is Formal Verification?

**Formal verification** uses mathematics and logic to prove that a smart contract always follows its intended rules.

Unlike testing, which checks only a few cases, formal verification proves correctness for **all possible inputs and states**.

This makes it one of the most powerful tools for securing blockchain smart contracts.

---

# Project Structure

```
contracts/        # Solidity smart contracts
specs/            # Certora CVL specification files
confs/            # Certora configuration files
```

---

# Setup Guide

## 1. Create a Python virtual environment

```bash
virtualenv certora-env
```

## 2. Activate the environment

```bash
source certora-env/bin/activate
```

You should see:

```
(certora-env)
```

in your terminal prompt.

---

## 3. Install Certora CLI

```bash
pip3 install certora-cli
```

## 4. Install solc-select

```bash
pip3 install solc-select
```

---

# Verification Guide

Follow these steps whenever you want to verify a contract.

## Step 1 — Activate the environment

```bash
source certora-env/bin/activate
```

---

## Step 2 — Run verification

You can verify contracts in **two ways**.

### Option A — Using a config file (recommended)

```bash
certoraRun confs/counter.conf
```

---

### Option B — Direct CLI command (example)

Below is a **sample verification command** using the `Counter` contract:

```bash
certoraRun contracts/Counter.sol --verify Counter:specs/counter.spec
```

Use this general format to verify **any contract**:

```
certoraRun <path-to-contract> --verify <ContractName>:<path-to-spec>
```

---

## Step 3 — View results

After running verification:

* Certora checks Solidity and CVL files for errors
* A **Certora Dashboard link** is generated in the CLI output
* Open the dashboard to see:

  * Mathematical proof results
  * `assert` rule verification
  * `satisfy` rule verification

If all rules pass, the contract logic is **formally proven to be correct** under the specification.

---

# Example Purpose

The `Counter` contract and its specification are included **as a learning example** to show how Certora verification works in practice.

Use this example as a reference when writing your own:

* Solidity contracts
* CVL specifications
* Verification configuration files

---

# Requirements

* Python 3.x
* pip3
* Solidity compiler (managed via `solc-select`)
* Certora Prover account and API access

---

# Learn More

* Certora Documentation: [https://docs.certora.com](https://docs.certora.com)
* RareSkills Certora Guide: [https://rareskills.io/tutorials/certora-book](https://rareskills.io/tutorials/certora-book)

---

# License

This project is provided for **educational and research purposes**.

Feel free to use it as a starting point for learning **smart contract formal verification with Certora**.
