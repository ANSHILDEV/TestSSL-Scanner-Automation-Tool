import subprocess

# List of domains and their associated ports for scanning
targets = {
    "api.prod.payglocal.in": [443, 2053, 2083, 2087, 2096, 8443],
    "apih.payglocal.in": [443, 2053, 2083, 2087, 2096, 8443],
    "api.pygcl.com": [443, 2053, 2083, 2087, 2096, 8443],
    "apih.pygcl.com": [443, 2053, 2083, 2087, 2096, 8443],
}

def run_testssl(domain, port, output_file):
    """
    Runs testssl on the given domain and port and saves the output to a file.
    """
    print(f"\nStarting testssl scan for {domain} on port {port}...")
    try:
        # Execute the testssl command and save the output to the file
        with open(output_file, "a") as f:
            f.write(f"\nStarting testssl scan for {domain} on port {port}...\n")
            subprocess.run(["testssl", f"{domain}:{port}"], stdout=f, stderr=f, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running testssl for {domain} on port {port}: {e}")
    except FileNotFoundError:
        print("Error: testssl tool not found. Please ensure it is installed and in your PATH.")

def main():
    """
    Iterates over targets and runs testssl scans, saving the output to a file.
    """
    output_file = "testssl_scan_results.txt"  # Output file to save results
    with open(output_file, "w") as f:
        f.write("TestSSL Scan Results\n")
        f.write("=" * 50 + "\n")
    
    for domain, ports in targets.items():
        for port in ports:
            run_testssl(domain, port, output_file)
    
    print(f"\nAll results have been saved to {output_file}")

if __name__ == "__main__":
    main()

