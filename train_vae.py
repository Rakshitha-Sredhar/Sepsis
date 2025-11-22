# import torch
# import torch.nn as nn
# import torch.optim as optim
# from model.vae_model import VAE
# from utils.preprocessing import preprocess_all_csvs
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import MinMaxScaler
# import joblib
# import numpy as np
# import os

# # Ensure save directory exists
# os.makedirs("saved_models", exist_ok=True)

# # Load data
# columns = ['HR', 'O2Sat', 'Resp', 'Temp', 'MAP', 'WBC', 'Platelets']
# X, _ = preprocess_all_csvs('data/converted_csvs', columns)
# print("Shape of preprocessed data:", X.shape)

# # Normalize data
# scaler = MinMaxScaler()
# X_scaled = scaler.fit_transform(X)

# # Convert to torch tensors
# X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
# train_data, val_data = train_test_split(X_tensor, test_size=0.2, random_state=42)

# # Model, loss, optimizer
# input_dim = X.shape[1]
# latent_dim = 8  # can increase later
# model = VAE(input_dim, latent_dim)
# optimizer = optim.Adam(model.parameters(), lr=1e-3)
# loss_fn = nn.MSELoss(reduction='sum')  # reconstruction loss

# # VAE loss function
# def vae_loss(recon_x, x, mu, logvar):
#     recon_loss = loss_fn(recon_x, x)
#     kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
#     return recon_loss + kl_loss

# # Training loop
# epochs = 50
# for epoch in range(epochs):
#     model.train()
#     optimizer.zero_grad()
#     recon, mu, logvar = model(train_data)
#     loss = vae_loss(recon, train_data, mu, logvar)
#     loss.backward()
#     optimizer.step()

#     model.eval()
#     with torch.no_grad():
#         val_recon, _, _ = model(val_data)
#         val_loss = loss_fn(val_recon, val_data)

#     print(f"Epoch {epoch+1}/{epochs} - Train Loss: {loss.item():.2f}, Val Recon Loss: {val_loss.item():.2f}")

# # Save model
# torch.save(model.state_dict(), "saved_models/vae_trained.pt")

# # Save scaler
# joblib.dump(scaler, "saved_models/scaler.joblib")

# # --- Updated: Compute threshold using 95th percentile ---
# model.eval()
# with torch.no_grad():
#     val_recon, _, _ = model(val_data)
#     recon_errors = torch.sum((val_data - val_recon) ** 2, dim=1).numpy()

# threshold = np.percentile(recon_errors, 95)  # 95th percentile of validation errors
# joblib.dump(threshold, "saved_models/threshold.joblib")

# print(f"✅ Model, scaler, and threshold saved to saved_models/ (threshold={threshold:.4f})")

import torch
import torch.nn as nn
import torch.optim as optim
from model.vae_model import VAE
from utils.preprocessing import preprocess_all_csvs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib
import numpy as np
import os

# Ensure save directory exists
os.makedirs("saved_models", exist_ok=True)

# -----------------------------
# Load and preprocess data
# -----------------------------
columns = ['HR', 'O2Sat', 'Resp', 'Temp', 'MAP', 'WBC', 'Platelets']
X, _ = preprocess_all_csvs('data/converted_csvs', columns)
print("Shape of preprocessed data:", X.shape)

# Normalize data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Convert to torch tensors
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
train_data, val_data = train_test_split(X_tensor, test_size=0.2, random_state=42)

# -----------------------------
# VAE model
# -----------------------------
input_dim = X.shape[1]
latent_dim = 8
model = VAE(input_dim, latent_dim)
optimizer = optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss(reduction='sum')

def vae_loss(recon_x, x, mu, logvar):
    recon_loss = loss_fn(recon_x, x)
    kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return recon_loss + kl_loss

# -----------------------------
# Training loop
# -----------------------------
epochs = 50
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    recon, mu, logvar = model(train_data)
    loss = vae_loss(recon, train_data, mu, logvar)
    loss.backward()
    optimizer.step()

    model.eval()
    with torch.no_grad():
        val_recon, _, _ = model(val_data)
        val_loss = loss_fn(val_recon, val_data)

    print(f"Epoch {epoch+1}/{epochs} - Train Loss: {loss.item():.2f}, Val Recon Loss: {val_loss.item():.2f}")

# -----------------------------
# Save model and scaler
# -----------------------------
torch.save(model.state_dict(), "saved_models/vae_trained.pt")
joblib.dump(scaler, "saved_models/scaler.joblib")

# -----------------------------
# Compute safe threshold
# -----------------------------
model.eval()
with torch.no_grad():
    val_recon, _, _ = model(val_data)
    recon_errors = torch.sum((val_data - val_recon) ** 2, dim=1).numpy()

# Use 99th percentile to avoid false positives for normal patients
threshold = np.percentile(recon_errors, 99)
joblib.dump(threshold, "saved_models/threshold.joblib")
print(f"✅ Model, scaler, and threshold saved to saved_models/ (threshold={threshold:.4f})")

# -----------------------------
# Optional: print some example recon errors
# -----------------------------
print("Sample reconstruction errors (first 10 validation samples):")
print(recon_errors[:10])
