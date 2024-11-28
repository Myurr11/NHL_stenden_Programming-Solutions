import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from IPython.display import display
import time

class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(100, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 784),
            nn.Tanh(),
        )

    def forward(self, x):
        output = self.model(x)
        output = output.view(x.size(0), 1, 28, 28)
        return output

class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(784, 1024),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        x = x.view(x.size(0), 784)
        output = self.model(x)
        return output

def train_gan(batch_size: int = 32, num_epochs: int = 100, device: str = "cuda:0" if torch.cuda.is_available() else "cpu"):
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    # Download MNIST dataset
    train_set = torchvision.datasets.MNIST(root=".", train=True, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)

    # Visualize a batch of real images
    real_samples, mnist_labels = next(iter(train_loader))
    fig = plt.figure()
    for i in range(16):
        sub = fig.add_subplot(4, 4, 1 + i)
        sub.imshow(real_samples[i].reshape(28, 28), cmap="gray_r")
        sub.axis('off')

    fig.tight_layout()
    fig.suptitle("Real images")
    display(fig)

    # Set up training
    discriminator = Discriminator().to(device)
    generator = Generator().to(device)
    lr = 0.0001
    loss_function = nn.BCELoss()
    optimizer_discriminator = torch.optim.Adam(discriminator.parameters(), lr=lr)
    optimizer_generator = torch.optim.Adam(generator.parameters(), lr=lr)

    # Print the device being used for training
    print(f"Using device: {device}")

    # Train GAN
    for epoch in range(num_epochs):
        for n, (real_samples, mnist_labels) in enumerate(train_loader):
            # Data for training the discriminator
            real_samples = real_samples.to(device=device)
            real_samples_labels = torch.ones((real_samples.size(0), 1)).to(device=device)
            latent_space_samples = torch.randn((real_samples.size(0), 100)).to(device=device)
            generated_samples = generator(latent_space_samples)
            generated_samples_labels = torch.zeros((real_samples.size(0), 1)).to(device=device)
            all_samples = torch.cat((real_samples, generated_samples))
            all_samples_labels = torch.cat((real_samples_labels, generated_samples_labels))

            # Training the discriminator
            discriminator.zero_grad()
            output = discriminator(all_samples)
            loss_discriminator = loss_function(output, all_samples_labels)
            loss_discriminator.backward()
            optimizer_discriminator.step()

            # Training the generator
            generator.zero_grad()
            latent_space_samples = torch.randn((real_samples.size(0), 100)).to(device=device)
            generated_samples = generator(latent_space_samples)
            output = discriminator(generated_samples)
            loss_generator = -torch.mean(torch.log(output))  # Improved stability for the generator
            loss_generator.backward()
            optimizer_generator.step()

        # Print progress
        print(f"Epoch [{epoch}/{num_epochs}] Loss D: {loss_discriminator.item()}, Loss G: {loss_generator.item()}")

        # Visualize generated images periodically
        if (epoch + 1) % 10 == 0:  # Show generated images every 10 epochs
            with torch.no_grad():
                latent_space_samples = torch.randn(16, 100).to(device)
                generated_samples = generator(latent_space_samples)
                fig = plt.figure(figsize=(4, 4))
                for i in range(16):
                    sub = fig.add_subplot(4, 4, i + 1)
                    sub.imshow(generated_samples[i].cpu().detach().numpy().reshape(28, 28), cmap="gray_r")
                    sub.axis('off')
                fig.tight_layout()
                fig.suptitle(f"Generated images at Epoch {epoch + 1}")
                display(fig)

# Run GAN Training
train_gan()
