"""
Demo: Dihedral Angle Analysis with FastMDAnalysis

This demo shows how to compute and plot average phi, psi, and omega backbone
dihedral angles per residue from an MD trajectory, including Ramachandran plots.
"""

from fastmdanalysis import FastMDAnalysis
import fastmdanalysis.datasets as ds

def main():
    # Load TrpCage dataset (small protein, fast for demo)
    traj_path = ds.TrpCage.traj
    top_path = ds.TrpCage.top

    # Create FastMDAnalysis instance with subsampling for speed
    fastmda = FastMDAnalysis(traj_path, top_path, frames=(0, -1, 10))

    print("Trajectory loaded:", fastmda.traj)
    print("Number of residues:", fastmda.traj.n_residues)

    # Analyze phi angles
    print("\n--- Phi Analysis ---")
    phi_analysis = fastmda.phi()
    print(f"Phi angles shape: {phi_analysis.data.shape}")
    print(f"Mean phi: {phi_analysis.data.mean():.2f}°")
    phi_plot = phi_analysis.plot(title="Average Phi Angles - TrpCage")
    print(f"Phi plot saved: {phi_plot}")

    # Analyze psi angles
    print("\n--- Psi Analysis ---")
    psi_analysis = fastmda.psi()
    print(f"Psi angles shape: {psi_analysis.data.shape}")
    print(f"Mean psi: {psi_analysis.data.mean():.2f}°")
    psi_plot = psi_analysis.plot(title="Average Psi Angles - TrpCage")
    print(f"Psi plot saved: {psi_plot}")

    # Analyze omega angles
    print("\n--- Omega Analysis ---")
    omega_analysis = fastmda.omega()
    print(f"Omega angles shape: {omega_analysis.data.shape}")
    print(f"Mean omega: {omega_analysis.data.mean():.2f}°")
    omega_plot = omega_analysis.plot(title="Average Omega Angles - TrpCage")
    print(f"Omega plot saved: {omega_plot}")

    # Combined analysis with Ramachandran plot
    print("\n--- Combined Dihedral Analysis ---")
    dihedrals_analysis = fastmda.dihedrals()
    print("Available data keys:", list(dihedrals_analysis.data.keys()))
    ramachandran_plot = dihedrals_analysis.plot()
    print(f"Ramachandran plot saved: {ramachandran_plot}")

    # Example: Analyze specific residues
    print("\n--- Analysis of Specific Residues ---")
    phi_res5 = fastmda.phi(residues=5)
    print(f"Phi for residue 5: {phi_res5.data[0,0]:.2f}°")

    # Highlight specific residues in plot
    phi_highlighted = fastmda.phi()
    highlighted_plot = phi_highlighted.plot(
        highlight_residues=[5, 10, 15],
        title="Phi Angles with Residues 5, 10, 15 Highlighted"
    )
    print(f"Highlighted plot saved: {highlighted_plot}")

if __name__ == "__main__":
    main()