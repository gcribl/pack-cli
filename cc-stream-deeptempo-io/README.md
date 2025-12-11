# DeepTempo NetFlow Pack

⸻

This Pack enables Cribl Stream users to forward normalized NetFlow data directly to DeepTempo for advanced network threat detection.
By leveraging DeepTempo’s foundation model (LogLM), this Pack allows organizations to identify command-and-control (C2), exfiltration, and other attack behaviors from network flow logs with high accuracy.

Once configured, Cribl Stream will collect and normalize NetFlow data, then tee it to a DeepTempo S3 destination for processing. DeepTempo performs sequence construction and inference on the data, returning enriched alerts or indicators that can be routed back through Cribl Stream to the customer’s SIEM or analytics platform.

## About this Pack

### Key Benefits:
	•	Seamlessly integrates Cribl Stream with DeepTempo’s AI-powered network analytics platform.
	•	Offloads NetFlow ingestion and normalization to Cribl, reducing custom parsing logic.
	•	Supports scalable data forwarding to DeepTempo’s S3-based interface for model inference.
	•	Enables attack-specific detection powered by DeepTempo’s LogLM foundation model, tuned for C2 and exfiltration behavior.
	•	Preserves your standard Cribl routing and replay patterns — minimal operational friction.

## Deployment

After installing this Pack:

	1.	Configure the NetFlow Source
	•	Add or verify your NetFlow data source in Cribl Stream.
	2.	Configure the DeepTempo S3 Destination
	•	DeepTempo uses a s3 prefix format of streaming/${tenant_name}/ - update the s3 prefix in the destination to include your organization's name.
	•	Contact DeepTempo to enable model processing on the prefix location. We support multiple methods of procurement (AWS Marketplace, Direct, etc.)
	3.	Enable Routing
	•	Apply the included Route from NetFlow Source → DeepTempo S3 Destination.
	•	Optionally tee data to other internal destinations (SIEM, data lake, etc.).

Once configured, Cribl Stream will automatically forward normalized NetFlow data to DeepTempo for inference.
If your organization is an onboarded DeepTempo customer, DeepTempo will pass this data through its LogLM model to identify active attacks, and will return enriched results back to Cribl Stream for downstream integration.

## Upgrades

Future releases of this Pack will include:
	•	Optional inline HTTP integration for inference callbacks.
	•	Sample enrichment pipelines for alert ingestion back into Stream.
	•	Support for Cribl Lake / Lakehouse ingestion and Replay workflows.

Upgrading is straightforward — replace the Pack in Cribl Stream.
Refer to Upgrading an Existing Pack￼ for best practices.

## Release Notes

### Version 0.9.0 - 2025-10-31
	•	Initial beta release of the DeepTempo NetFlow Pack.
	•	Added route for NetFlow → DeepTempo S3.
	•	Includes Pack metadata, configuration template, and README.

## Contributing to the Pack

To contribute improvements, raise feature requests, or report issues, please reach out directly to the DeepTempo engineering team.
	•	Contact: Sam Armstrong
	•	Email: [sam@deeptempo.ai](mailto:sam@deeptempo.ai)
	•	Website: [https://www.deeptempo.ai](https://www.deeptempo.ai)

## Contact

For technical support or partnership inquiries, please email [sam@deeptempo.ai](mailto:sam@deeptempo.ai).

## License

This Pack uses the following license: [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).