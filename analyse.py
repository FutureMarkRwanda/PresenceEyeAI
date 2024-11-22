import matplotlib.pyplot as plt
import pandas as pd

# Load your CSV data
df = pd.read_csv("Week_1/train/results.csv")

# Extract relevant columns
epochs = df['epoch']
train_loss = df['train/box_loss'] + df['train/cls_loss'] + df['train/dfl_loss']
val_mAP = df['metrics/mAP50(B)']

# Calculate averages
average_train_loss = train_loss.mean()
average_val_mAP = val_mAP.mean()

# Print the averages
print(f"Average Training Loss: {average_train_loss:.4f}")
print(f"Average Validation mAP50(B): {average_val_mAP:.4f}")

# Plot training loss and validation mAP
plt.figure(figsize=(10, 5))

# Plot training loss
plt.subplot(1, 2, 1)
plt.plot(epochs, train_loss, label='Training Loss', color='blue')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss Over Epochs')
plt.legend()

# Plot validation mAP
plt.subplot(1, 2, 2)
plt.plot(epochs, val_mAP, label='Validation mAP50(B)', color='green')
plt.xlabel('Epoch')
plt.ylabel('mAP50(B)')
plt.title('Validation mAP50(B) Over Epochs')
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()

# Output the Training Loss and Validation mAP per epoch
for epoch, loss, mAP in zip(epochs, train_loss, val_mAP):
    print(f"Epoch {epoch}: Training Loss = {loss:.4f}, Validation mAP50(B) = {mAP:.4f}")
