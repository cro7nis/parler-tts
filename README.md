# Text-to-Speech with Parler-TTS
Text-to-Speech app powerered by [parler-tts library](https://github.com/huggingface/parler-tts) and [Streamlit](https://streamlit.io/).

The project is developed for the **Deploy a TTS solution on Akash** zealy task which is hosted by [Akash](https://zealy.io/cw/akashnetwork/questboard).

## Deploy on Akash guide <img src="./assets/akash-logo.png" alt="drawing" width=20 height=20/> 



https://github.com/cro7nis/parler-tts/assets/166608635/d916a91d-eb91-41f0-8601-0c657b8be574



- Create and fund a Keplr or Leap wallet
  - [Keplr wallet](https://akash.network/docs/getting-started/token-and-wallets/#keplr-wallet)
  - [Leap wallet](https://akash.network/docs/getting-started/token-and-wallets/#leap-cosmos-wallet)
- Visit https://deploy.cloudmos.io/
- Connect your wallet
  - You need to have at least 0.5 AKT in your wallet
- Press the deploy button
- Select "Build your template"
- (Optional) Name your deployment
- Select YAML and paste the [deploy.yaml](deploy.yaml) contents
- Press "Create Deployment"
- Accept wallet transaction
- Review bids and select provider
- Accept provider transaction
- Go to LEASES and press the URI
- Check the [Akash docs](https://akash.network/docs/deployments/cloudmos-deploy/) if you have and questions
- Start generating speech!
  - Add the input text for speech generation
  - Provide a description of the speaker to adapt the generated voice
