curl https://pyenv.run | bash

echo "" >> ~/.bashrc
echo "# Automatically setup pyenv" >> ~/.bashrc
echo "export PATH=\"/root/.pyenv/bin:\$PATH\"" >> ~/.bashrc
echo "eval \"\$(pyenv init -)\"" >> ~/.bashrc
echo "eval \"\$(pyenv virtualenv-init -)\"" >> ~/.bashrc

. ~/.bashrc
