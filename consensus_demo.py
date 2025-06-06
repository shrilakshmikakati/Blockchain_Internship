import random
import json
from typing import Dict, List, Any

class ConsensusSimulator:
    def __init__(self):
        """Initialize the consensus mechanism simulator"""
        self.reset_validators()
    
    def reset_validators(self):
        """Reset all validator data with random values"""
        self.miners = [
            {"id": "Miner_A", "power": random.randint(100, 1000)},
            {"id": "Miner_B", "power": random.randint(100, 1000)},
            {"id": "Miner_C", "power": random.randint(100, 1000)}
        ]

        self.stakers = [
            {"id": "Staker_Alpha", "stake": random.randint(1000, 10000)},
            {"id": "Staker_Beta", "stake": random.randint(1000, 10000)},
            {"id": "Staker_Gamma", "stake": random.randint(1000, 10000)}
        ]

        self.delegates = [
            {"id": "Delegate_X", "votes": 0},
            {"id": "Delegate_Y", "votes": 0},
            {"id": "Delegate_Z", "votes": 0}
        ]

        self.voters = [
            {"id": "Voter_1", "voting_power": random.randint(50, 500)},
            {"id": "Voter_2", "voting_power": random.randint(50, 500)},
            {"id": "Voter_3", "voting_power": random.randint(50, 500)}
        ]

        self.simulate_voting()
    
    def simulate_voting(self):
        """Simulate the voting process for DPoS"""
        for voter in self.voters:
            chosen_delegate = random.choice(self.delegates)
            chosen_delegate["votes"] += voter["voting_power"]
            print(f"[VOTE] {voter['id']} votes for {chosen_delegate['id']} with {voter['voting_power']} voting power")
    
    def proof_of_work_consensus(self) -> Dict[str, Any]:
        """Simulate Proof of Work consensus mechanism"""
        print("\n" + "="*50)
        print("PROOF OF WORK (PoW) SIMULATION")
        print("="*50)
        
        print("Miners and their hash power:")
        for miner in self.miners:
            print(f"  * {miner['id']}: {miner['power']} TH/s")
  
        selected_miner = max(self.miners, key=lambda x: x['power'])
        
        selection_explanation = (
            "PoW Selection Logic: In Proof of Work, the miner with the highest "
            "computational power (hash rate) has the best chance of solving the "
            "cryptographic puzzle first and mining the next block."
        )
        
        print(f"\n[WINNER] Selected Validator: {selected_miner['id']}")
        print(f"[POWER] Hash Power: {selected_miner['power']} TH/s")
        print(f"[LOGIC] {selection_explanation}")
        
        return {
            "mechanism": "Proof of Work",
            "selected_validator": selected_miner,
            "selection_criteria": "Highest computational power",
            "explanation": selection_explanation
        }
    
    def proof_of_stake_consensus(self) -> Dict[str, Any]:
        """Simulate Proof of Stake consensus mechanism"""
        print("\n" + "="*50)
        print("PROOF OF STAKE (PoS) SIMULATION")
        print("="*50)
        
        print("Stakers and their stake amounts:")
        for staker in self.stakers:
            print(f"  * {staker['id']}: {staker['stake']} tokens")

        total_stake = sum(staker['stake'] for staker in self.stakers)

        selected_staker = max(self.stakers, key=lambda x: x['stake'])
        
        print(f"\nStake probabilities:")
        for staker in self.stakers:
            probability = (staker['stake'] / total_stake) * 100
            print(f"  * {staker['id']}: {probability:.1f}%")
        
        selection_explanation = (
            "PoS Selection Logic: In Proof of Stake, validators are chosen to create "
            "new blocks based on their stake in the network. Higher stake = higher "
            "probability of being selected. This saves energy compared to PoW."
        )
        
        print(f"\n[WINNER] Selected Validator: {selected_staker['id']}")
        print(f"[STAKE] Stake Amount: {selected_staker['stake']} tokens")
        print(f"[LOGIC] {selection_explanation}")
        
        return {
            "mechanism": "Proof of Stake",
            "selected_validator": selected_staker,
            "selection_criteria": "Probabilistic based on stake amount",
            "explanation": selection_explanation
        }
    
    def delegated_proof_of_stake_consensus(self) -> Dict[str, Any]:
        """Simulate Delegated Proof of Stake consensus mechanism"""
        print("\n" + "="*50)
        print("DELEGATED PROOF OF STAKE (DPoS) SIMULATION")
        print("="*50)
        
        print("Voting results:")
        for delegate in self.delegates:
            print(f"  * {delegate['id']}: {delegate['votes']} votes")

        selected_delegate = max(self.delegates, key=lambda x: x['votes'])
        
        selection_explanation = (
            "DPoS Selection Logic: In Delegated Proof of Stake, token holders vote "
            "for delegates who will validate transactions on their behalf. The "
            "delegates with the most votes become the active validators."
        )
        
        print(f"\n[WINNER] Selected Validator: {selected_delegate['id']}")
        print(f"[VOTES] Total Votes: {selected_delegate['votes']}")
        print(f"[LOGIC] {selection_explanation}")
        
        return {
            "mechanism": "Delegated Proof of Stake",
            "selected_validator": selected_delegate,
            "selection_criteria": "Most votes from token holders",
            "explanation": selection_explanation
        }
    
    def compare_mechanisms(self):
        """Compare all three consensus mechanisms"""
        print("\n" + "="*60)
        print("CONSENSUS MECHANISM COMPARISON")
        print("="*60)
        
        pow_result = self.proof_of_work_consensus()
        pos_result = self.proof_of_stake_consensus()
        dpos_result = self.delegated_proof_of_stake_consensus()
        
        print("\n" + "="*60)
        print("SUMMARY COMPARISON")
        print("="*60)
        
        mechanisms = [pow_result, pos_result, dpos_result]
        
        for result in mechanisms:
            print(f"\n[{result['mechanism']}]:")
            print(f"   Winner: {result['selected_validator']['id']}")
            print(f"   Criteria: {result['selection_criteria']}")

        print("\nKEY DIFFERENCES:")
        print("* PoW: Energy-intensive, secure through computational work")
        print("* PoS: Energy-efficient, secure through economic stake")
        print("* DPoS: Fast and scalable, democratic through voting")
        
        return {
            "pow": pow_result,
            "pos": pos_result,
            "dpos": dpos_result
        }
    
    def run_simulation(self):
        """Run the complete consensus mechanism simulation"""
        print("Starting Blockchain Consensus Mechanism Simulation")
        print("=" * 60)
        
        return self.compare_mechanisms()

# Run the simulation
if __name__ == "__main__":
    simulator = ConsensusSimulator()
    results = simulator.run_simulation()
 