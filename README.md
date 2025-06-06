# Blockchain_Internship

This repository contains three blockchain simulation projects to understand core blockchain concepts through hands-on coding exercises.
Contents
# 1. Block Simulation (block_simulation.py)
   
Objective: Build a basic blockchain with 3 linked blocks using code.
Features:

Block class with index, timestamp, data, previousHash, hash, and nonce
SHA-256 hash generator implementation
3 blocks linked by chaining their previousHash
Display all blocks with their hashes
Challenge: Change data of Block 1 and observe how following blocks become invalid

Goal: Understand how tampering one block affects the entire chain.
# 2. Nonce Mining Simulation (mining_simulation.py)

Objective: Simulate Proof-of-Work by mining a block that satisfies a difficulty condition.
Features:

Block class with mineBlock(difficulty) function
Set difficulty (hash must start with specific number of zeros)
Increment nonce until hash meets difficulty condition
Print nonce attempts needed and time taken

Goal: Experience how computational effort increases with difficulty.
# 3. Consensus Mechanism Simulation (consensus_simulation.py)

Objective: Simulate and compare PoW, PoS, and DPoS logic in code.
Features:

Mock objects for 3 validators:

PoW: miner with random power values
PoS: staker with random stake values
DPoS: voters with 3 mock accounts voting


Selection logic:

PoW: Select validator with highest power
PoS: Select validator with highest stake
DPoS: Choose delegate based on most votes


Print selected validator and consensus method with explanation

Goal: Compare decision-making in various consensus mechanisms.
