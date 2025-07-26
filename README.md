# mcp-test

This repository is for MCP test and experiments.

Feel free to add your notes, code, or documentation here.

## How to Add a Kubernetes MCP Server to VS Code

1. **Install Prerequisites**
   - Install [Docker](https://www.docker.com/) and [kubectl](https://kubernetes.io/docs/tasks/tools/).
   - Install the [Kubernetes extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-kubernetes-tools.vscode-kubernetes-tools).

2. **Deploy MCP Server to Kubernetes**
   - Create a Kubernetes deployment YAML for your MCP server (or use an existing one).
   - Apply the deployment:
     ```sh
     kubectl apply -f <your-mcp-server-deployment.yaml>
     ```
   - Expose the service if needed:
     ```sh
     kubectl expose deployment <mcp-server-deployment> --type=LoadBalancer --port=8080
     ```

3. **Connect to the Cluster in VS Code**
   - Open VS Code and click on the Kubernetes extension icon.
   - Make sure your kubeconfig is set up and points to the correct cluster.
   - You should see your MCP server pod/service listed in the extension.

4. **Access and Manage MCP Server**
   - Use the extension to view logs, port-forward, or manage the MCP server.
   - For port-forwarding:
     ```sh
     kubectl port-forward svc/<mcp-server-service> 8080:8080
     ```
   - Access the MCP server at `http://localhost:8080` in your browser or API client.

5. **(Optional) Use GitHub Copilot**
   - Install the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) for code assistance while working with your MCP server code.

---

For more details, refer to the official documentation of Kubernetes, VS Code extensions, and your MCP server.
