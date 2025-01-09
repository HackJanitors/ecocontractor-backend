from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import os
from huggingface_hub import InferenceClient

router = APIRouter()

# Hugging Face API Client Initialization
HF_TOKEN = "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"
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN,
)

class ContractParams(BaseModel):
    issuer: str
    buyer: str
    verifier: str
    project_metadata: dict
    retirement_status: str

def generate_solidity_contract(params):
    """Generate a Solidity smart contract based on user parameters"""
    prompt = f"""
    Generate a complete Solidity smart contract for carbon credits with the following parameters:
    Issuer: {params['issuer']}
    Buyer: {params['buyer']}
    Verifier: {params['verifier']}
    Location: {params['project_metadata']['location']}
    Project Type: {params['project_metadata']['type']}
    Certification Body: {params['project_metadata']['certification']}
    Retirement Status: {params['retirement_status']}

    The contract should include:
    1. SPDX License Identifier and pragma statement
    2. Import statements for OpenZeppelin contracts
    3. Contract inheritance from ERC-721 for NFT functionality
    4. State variables for all parameters
    5. Events for important state changes
    6. Constructor
    7. Functions for:
    - Minting new carbon credits
    - Transferring credits
    - Retiring credits
    - Verifying project status
    - Getting project metadata
    8. Access control modifiers
    9. Input validation
    10. Error handling

    Generate the complete Solidity code:
    """

    # Generate contract
    response = client.text_generation(
        prompt,
        max_new_tokens=1500,
        temperature=0.2,  # Lower temperature for more consistent output
        do_sample=True
    )

    return response

def save_contract(contract_code, params):
    """Save the generated contract to a file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"CarbonCredit_{params['issuer'].replace(' ', '')}_v{timestamp}.sol"

    with open(filename, 'w') as f:
        f.write(contract_code)

    return filename

@router.post("/generate_contract/")
async def generate_contract(params: ContractParams):
    try:
        contract_code = generate_solidity_contract(params.dict())
        filename = save_contract(contract_code, params.dict())

        return {
            "message": "Smart Contract Generated Successfully!",
            "filename": filename,
            "contract_code": contract_code
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
