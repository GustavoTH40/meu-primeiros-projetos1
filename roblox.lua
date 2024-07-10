-- this is an example for the script, use this to make your own! (Might be adding custom Themes)
local Lib = loadstring(game:HttpGet("https://raw.githubusercontent.com/7yhx/kwargs_Ui_Library/main/source.lua"))()

local UI = Lib:Create{
   Theme = "Dark", -- or any other theme
   Size = UDim2.new(0, 555, 0, 400) -- default
}

local Main = UI:Tab{
   Name = "Inicio"
}

local Divider = Main:Divider{
   Name = "Inicio shit"
}

local QuitDivider = Main:Divider{
   Name = "Sair
}

-- All functions have the Name, Description and Callback arguments so you can use them whenever ig yeah
local KillAll = Divider:Button{
   Name = "Kill all",
   Description = "Kills all the players in the game!",
   Callback = function()
       print("All players killed.")
   end
}
