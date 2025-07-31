#!/usr/bin/env python3
"""
Kubernetes Architecture Diagram Generator
Creates a PNG diagram of the K8S infrastructure setup
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

def create_architecture_diagram():
    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Colors
    aws_orange = '#FF9900'
    docker_blue = '#2496ED'
    k8s_blue = '#326CE5'
    nginx_green = '#009639'
    app_purple = '#7B68EE'
    
    # Title
    ax.text(8, 11.5, 'Kubernetes Development Environment Architecture', 
            fontsize=20, fontweight='bold', ha='center')
    ax.text(8, 11, 'AWS EC2 + Docker + kind + Applications', 
            fontsize=14, ha='center', style='italic')
    
    # External Access Layer
    external_box = FancyBboxPatch((0.5, 9.5), 15, 1.2, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor='lightblue', 
                                  edgecolor='blue', linewidth=2)
    ax.add_patch(external_box)
    ax.text(8, 10.1, '🌐 EXTERNAL ACCESS', fontsize=14, fontweight='bold', ha='center')
    ax.text(8, 9.7, 'Browser: http://13.126.208.59:8080 (nginx) | :8090 (online-shop)', 
            fontsize=11, ha='center')
    
    # AWS EC2 Instance
    ec2_box = FancyBboxPatch((1, 7), 14, 2, 
                             boxstyle="round,pad=0.1", 
                             facecolor=aws_orange, 
                             edgecolor='darkorange', linewidth=2, alpha=0.3)
    ax.add_patch(ec2_box)
    ax.text(8, 8.5, '🖥️ AWS EC2 Instance', fontsize=16, fontweight='bold', ha='center')
    ax.text(8, 8.1, 'Ubuntu 24.04 LTS (t2.micro) | 1 vCPU, 1GB RAM', fontsize=11, ha='center')
    ax.text(8, 7.7, 'Region: ap-south-1 (Mumbai) | Public IP: 13.126.208.59', fontsize=11, ha='center')
    ax.text(8, 7.3, 'Security Group: SSH (22), HTTP (8080, 8090)', fontsize=10, ha='center')
    
    # Docker Engine
    docker_box = FancyBboxPatch((1.5, 5.5), 13, 1.2, 
                                boxstyle="round,pad=0.1", 
                                facecolor=docker_blue, 
                                edgecolor='darkblue', linewidth=2, alpha=0.3)
    ax.add_patch(docker_box)
    ax.text(8, 6.3, '🐳 Docker Engine v27.5.1', fontsize=14, fontweight='bold', ha='center')
    ax.text(8, 5.9, 'Container Runtime | Bridge Network: 172.18.0.0/16', fontsize=11, ha='center')
    
    # kind Cluster
    kind_box = FancyBboxPatch((2, 2), 12, 3.2, 
                              boxstyle="round,pad=0.1", 
                              facecolor=k8s_blue, 
                              edgecolor='darkblue', linewidth=2, alpha=0.2)
    ax.add_patch(kind_box)
    ax.text(8, 4.8, '⚙️ kind Cluster (dev-cluster)', fontsize=14, fontweight='bold', ha='center')
    ax.text(8, 4.5, 'Kubernetes v1.32.0 | Single Node | Control Plane: dev-cluster-control-plane', 
            fontsize=10, ha='center')
    
    # nginx Namespace
    nginx_box = FancyBboxPatch((2.5, 3.2), 5, 1.5, 
                               boxstyle="round,pad=0.05", 
                               facecolor=nginx_green, 
                               edgecolor='darkgreen', linewidth=1, alpha=0.3)
    ax.add_patch(nginx_box)
    ax.text(5, 4.3, '📦 nginx Namespace', fontsize=12, fontweight='bold', ha='center')
    ax.text(5, 4.0, '• nginx-pod (1 replica)', fontsize=9, ha='center')
    ax.text(5, 3.8, '• ClusterIP Service', fontsize=9, ha='center')
    ax.text(5, 3.6, '• NodePort: 30080', fontsize=9, ha='center')
    ax.text(5, 3.4, '• Port Forward: 8080', fontsize=9, ha='center')
    
    # online-shop Namespace
    shop_box = FancyBboxPatch((8.5, 3.2), 5, 1.5, 
                              boxstyle="round,pad=0.05", 
                              facecolor=app_purple, 
                              edgecolor='purple', linewidth=1, alpha=0.3)
    ax.add_patch(shop_box)
    ax.text(11, 4.3, '📦 online-shop Namespace', fontsize=12, fontweight='bold', ha='center')
    ax.text(11, 4.0, '• Deployment: 3 replicas', fontsize=9, ha='center')
    ax.text(11, 3.8, '• ClusterIP + NodePort', fontsize=9, ha='center')
    ax.text(11, 3.6, '• NodePort: 30090', fontsize=9, ha='center')
    ax.text(11, 3.4, '• Port Forward: 8090', fontsize=9, ha='center')
    
    # System Pods
    system_box = FancyBboxPatch((2.5, 2.2), 11, 0.8, 
                                boxstyle="round,pad=0.05", 
                                facecolor='lightgray', 
                                edgecolor='gray', linewidth=1, alpha=0.5)
    ax.add_patch(system_box)
    ax.text(8, 2.7, '🔧 System Pods', fontsize=11, fontweight='bold', ha='center')
    ax.text(8, 2.4, 'kube-apiserver | etcd | kube-scheduler | kube-controller | coredns | kube-proxy | kindnet', 
            fontsize=9, ha='center')
    
    # Traffic Flow Arrows
    # External to EC2
    ax.annotate('', xy=(8, 9.4), xytext=(8, 8.6), 
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    
    # EC2 to Docker
    ax.annotate('', xy=(8, 7), xytext=(8, 6.7), 
                arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
    
    # Docker to kind
    ax.annotate('', xy=(8, 5.3), xytext=(8, 5.0), 
                arrowprops=dict(arrowstyle='->', lw=2, color='green'))
    
    # Resource Usage Box
    resource_box = FancyBboxPatch((0.5, 0.2), 7, 1.5, 
                                  boxstyle="round,pad=0.05", 
                                  facecolor='lightyellow', 
                                  edgecolor='orange', linewidth=1)
    ax.add_patch(resource_box)
    ax.text(4, 1.5, '📊 Resource Usage', fontsize=12, fontweight='bold', ha='center')
    ax.text(4, 1.2, 'nginx: No limits (best effort)', fontsize=9, ha='center')
    ax.text(4, 1.0, 'online-shop: 750m CPU, 192Mi RAM (total)', fontsize=9, ha='center')
    ax.text(4, 0.8, 'System Pods: ~500m CPU, ~1Gi RAM', fontsize=9, ha='center')
    ax.text(4, 0.6, 'Total Cluster: ~1.25 CPU cores, ~1.2Gi RAM', fontsize=9, ha='center')
    ax.text(4, 0.4, 'EC2 Capacity: 1 vCPU, 1GB RAM (80% utilized)', fontsize=9, ha='center')
    
    # Access URLs Box
    access_box = FancyBboxPatch((8.5, 0.2), 7, 1.5, 
                                boxstyle="round,pad=0.05", 
                                facecolor='lightgreen', 
                                edgecolor='darkgreen', linewidth=1)
    ax.add_patch(access_box)
    ax.text(12, 1.5, '🌐 Access URLs', fontsize=12, fontweight='bold', ha='center')
    ax.text(12, 1.2, 'nginx: http://13.126.208.59:8080', fontsize=9, ha='center')
    ax.text(12, 1.0, 'online-shop: http://13.126.208.59:8090', fontsize=9, ha='center')
    ax.text(12, 0.8, 'Internal nginx: http://172.18.0.2:30080', fontsize=9, ha='center')
    ax.text(12, 0.6, 'Internal shop: http://172.18.0.2:30090', fontsize=9, ha='center')
    ax.text(12, 0.4, 'kubectl port-forward for external access', fontsize=9, ha='center')
    
    # Add version info
    ax.text(15.5, 0.5, 'v1.0.0\nJuly 2025', fontsize=8, ha='right', va='bottom', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    return fig

def main():
    print("🎨 Generating Kubernetes Architecture Diagram...")
    
    # Create the diagram
    fig = create_architecture_diagram()
    
    # Save as PNG
    output_file = 'kubernetes-architecture-diagram.png'
    fig.savefig(output_file, dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    print(f"✅ Diagram saved as: {output_file}")
    print(f"📏 High resolution (300 DPI) PNG created")
    
    # Also save as SVG for scalability
    svg_file = 'kubernetes-architecture-diagram.svg'
    fig.savefig(svg_file, format='svg', bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    print(f"✅ Vector version saved as: {svg_file}")
    
    plt.close()

if __name__ == "__main__":
    main()
