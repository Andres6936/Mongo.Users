import tkinter as tk
from tkinter import ttk


class PanelTLSSSL(tk.Frame):
    """
    The TLS / SSL tab allows you to connect deployments using
    TLS / SSL. You can leave TLS unset with the Default option
    or set the TLS / SSL connection On or Off.

    Option

    - Default: The Default option leaves the TLS option unset.
      The Default / unset TLS /SSL option is enabled when using
      a DNS seedlist (SRV) in the connection string.

    - On: Select the On option when using a DNS seedlist (SRV)
      in the connection string. When TLS / SSL Connection is
      On, you can specify additional certificate options for
      your connection string.

    - Off: The Off option initiates a connection without TLS / SSL.

    Note: It is recommended that users enable TLS / SSL to
    avoid security vulnerabilities.

    Additional TLS / SSL Options

    When TLS is On you can specify the following:

    - Certificate Authority: One or more certificate files from
      trusted Certificate Authorities to validate the certificate
      provided by the deployment.

    - Client Certificate: Specifies the location of a local .pem
      file that contains either the client's TLS/SSL X.509
      certificate or the client's TLS/SSL certificate and key.

    - Client Key Password: If the Client Private Key is protected
      with a password, you must provide the password.

    - tlsInsecure: Disables various certificate validations.

    - tlsAllowInvalidHostnames: Disables hostname validation of
      the certificate presented by the the deployment.

    - tlsAllowInvalidCertificates: Disable the validation of the
      server certificates.
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.grid_columnconfigure((0, 1, 2), uniform="uniform", weight=1)

        self.sslTLSConnection = tk.Label(self, text="SSL/TLS Connection")
        self.sslTLSConnection.grid(row=0, column=0, sticky=tk.W)

        self.buttonDefault = ttk.Button(self, text="Default")
        self.buttonDefault.grid(row=1, column=0)

        self.buttonOn = ttk.Button(self, text="On")
        self.buttonOn.grid(row=1, column=1)

        self.buttonOff = ttk.Button(self, text="Off")
        self.buttonOff.grid(row=1, column=2)

        self.labelCertificateAuthority = ttk.Label(self, text="Certificate Authority (.pem)")
        self.labelCertificateAuthority.grid(row=2, column=0, sticky=tk.W)

        self.fileCertificatePEM = ttk.Button(self, text="Select a file...")
        self.fileCertificatePEM.grid(row=2, column=1, columnspan=2, sticky=tk.W + tk.E, pady=5)

        self.labelClientCertificate = ttk.Label(self, text="Client Certificate and Key (.pem)")
        self.labelClientCertificate.grid(row=3, column=0, sticky=tk.W)

        self.fileClientCertificatePEM = ttk.Button(self, text="Select a file...")
        self.fileClientCertificatePEM.grid(row=3, column=1, columnspan=2, sticky=tk.W + tk.E, pady=1)

        self.labelClientKey = ttk.Label(self, text="Client Key Password")
        self.labelClientKey.grid(row=4, column=0, sticky=tk.W)

        self.inputClientPassword = ttk.Entry(self)
        self.inputClientPassword.grid(row=5, column=0, columnspan=3, sticky=tk.W + tk.E)

        self.checkInsecure = ttk.Checkbutton(self, text="tlsInsecure")
        self.checkInsecure.grid(row=6, sticky=tk.W)

        self.labelInsecure = ttk.Label(self,
                                       text="This includes tlsAllowInvalidHostnames and tlsAllowInvalidCertificates.")
        self.labelInsecure.grid(row=7, column=0, columnspan=3, sticky=tk.W)

        self.checkAllowInvalidHostnames = ttk.Checkbutton(self, text="tlsAllowInvalidHostnames")
        self.checkAllowInvalidHostnames.grid(row=8, sticky=tk.W)

        self.labelAllowInvalidHostnames = ttk.Label(self,
                                                    text="Disable the validation of the hostnames in the certificate presented by the mongod/mongos instance.")
        self.labelAllowInvalidHostnames.grid(row=9, column=0, columnspan=3, sticky=tk.W)

        self.checkAllowInvalidCertificates = ttk.Checkbutton(self, text="tlsAllowInvalidCertificates")
        self.checkAllowInvalidCertificates.grid(row=10, sticky=tk.W)

        self.labelAllowInvalidCertificates = ttk.Label(self, text="Disable the validation of the server certificates.")
        self.labelAllowInvalidCertificates.grid(row=11, column=0, columnspan=3, sticky=tk.W)
