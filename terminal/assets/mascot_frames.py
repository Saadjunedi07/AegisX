"""ANSI frame animations for Aegis.

The terminal avatar follows the same reference design as the Web mascot:
grey rocky upper half, beige stone lower half, tiny black dot eyes, short rock
arms and legs, a moss patch on the top-right, and a small green sprout.
"""

IDLE_FRAMES = [
    r"""
        [green]^^[/green]
      [green]/##\[/green]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][black].[/black][grey62]#######[/grey62][black].[/black][grey62]##o[/grey62]
 [tan]/##[/tan][grey35]__[/grey35][tan]######[/tan][grey35]__[/grey35][tan]##\[/tan]
 [tan]\##############/[/tan]
     [grey50]||[/grey50]      [grey50]||[/grey50]
""",
    r"""
        [green]^^[/green]
      [green]\##/[/green]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][black].[/black][grey62]#######[/grey62][black].[/black][grey62]##o[/grey62]
 [tan]/##[/tan][grey35]__[/grey35][tan]######[/tan][grey35]__[/grey35][tan]##\[/tan]
 [tan]\##############/[/tan]
    [grey50]||[/grey50]        [grey50]||[/grey50]
""",
    r"""
        [green]^^[/green]
      [green]/##\[/green]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][black]-[/black][grey62]#######[/grey62][black]-[/black][grey62]##o[/grey62]
 [tan]/##[/tan][grey35]__[/grey35][tan]######[/tan][grey35]__[/grey35][tan]##\[/tan]
 [tan]\##############/[/tan]
     [grey50]||[/grey50]      [grey50]||[/grey50]
""",
]

SCANNING_FRAMES = [
    r"""
        [green]^^[/green]   [dodger_blue1]scan[/dodger_blue1]
      [green]/##\[/green] [dodger_blue1]-----[/dodger_blue1]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o#[/grey62][dodger_blue1]>[/dodger_blue1][grey62]########[/grey62][dodger_blue1]<[/dodger_blue1][grey62]#o[/grey62]
 [tan]/##[/tan][dodger_blue1]==========[/dodger_blue1][tan]##\[/tan]
 [tan]\##############/[/tan]
     [grey50]||[/grey50]      [grey50]||[/grey50]
""",
    r"""
        [green]^^[/green]
      [green]\##/[/green]     [dodger_blue1]///[/dodger_blue1]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/[/grey62][dodger_blue1]==========[/dodger_blue1][grey62]\[/grey62][green]@@@@[/green]
[grey62]o#[/grey62][dodger_blue1]>[/dodger_blue1][grey62]########[/grey62][dodger_blue1]<[/dodger_blue1][grey62]#o[/grey62]
 [tan]/##############\[/tan]
 [tan]\##############/[/tan]
     [grey50]||[/grey50]      [grey50]||[/grey50]
""",
]

THINKING_FRAMES = [
    r"""
        [green]^^[/green]       [yellow]?[/yellow]
      [green]/##\[/green]    [yellow]...[/yellow]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][black].[/black][grey62]#######[/grey62][black].[/black][grey62]##o[/grey62]
 [tan]/#####~########\[/tan]
 [tan]\##############/[/tan]
     [grey50]||[/grey50]      [grey50]||[/grey50]
""",
    r"""
      [yellow]?[/yellow] [green]^^[/green]
      [green]\##/[/green]      [yellow]..[/yellow]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][black].[/black][grey62]#######[/grey62][black].[/black][grey62]##o[/grey62]
 [tan]/######o#######\[/tan]
 [tan]\##############/[/tan]
    [grey50]||[/grey50]        [grey50]||[/grey50]
""",
]

ALERT_FRAMES = [
    r"""
    [red bold]ALERT[/red bold]     [red]|>[/red]
        [green]^^[/green]
      [green]/##\[/green]
   [red]_/########\_[/red][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][red bold]o[/red bold][grey62]#######[/grey62][red bold]o[/red bold][grey62]##o[/grey62]
 [tan]/######O#######\[/tan]
 [tan]\##############/[/tan]
     [grey50]||[/grey50]      [grey50]||[/grey50]
""",
    r"""
    [red bold]ALERT[/red bold]   [red]|>[/red]
        [green]^^[/green]
      [green]\##/[/green]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [red]/############\[/red][green]@@@@[/green]
[grey62]o##[/grey62][red bold]O[/red bold][grey62]#######[/grey62][red bold]O[/red bold][grey62]##o[/grey62]
 [tan]/######o#######\[/tan]
 [tan]\##############/[/tan]
    [grey50]||[/grey50]        [grey50]||[/grey50]
""",
]

CRITICAL_FRAMES = [
    r"""
   [red bold]CRITICAL THREAT[/red bold]
        [red]^^[/red]      [red]|>[/red]
      [red]/##\[/red]
   [red]_/########\_[/red][green]@@@[/green]
 [red]/############\[/red][green]@@@@[/green]
[red]o##[/red][white bold]O[/white bold][red]#######[/red][white bold]O[/white bold][red]##o[/red]
 [tan]/#####[red]!!![/red][tan]######\[/tan]
 [tan]\##############/[/tan]
    [red]||[/red]        [red]||[/red]
""",
    r"""
 [red bold]!! CRITICAL THREAT !![/red bold]
        [red]^^[/red]   [red]|>[/red]
      [red]\##/[/red]
   [red]_/########\_[/red][green]@@@[/green]
 [red]/############\[/red][green]@@@@[/green]
[red]o##[/red][white bold]0[/white bold][red]#######[/red][white bold]0[/white bold][red]##o[/red]
 [tan]/#####[red]!!![/red][tan]######\[/tan]
 [tan]\##############/[/tan]
     [red]||[/red]      [red]||[/red]
""",
]

HEALING_FRAMES = [
    r"""
        [green]^^[/green]       [green]+[/green]
      [green]/##\[/green]   [grey85]==O[/grey85]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][black].[/black][grey62]#######[/grey62][black].[/black][grey62]##o[/grey62]
 [tan]/#####[green]___[/green][tan]######\[/tan]
 [tan]\##############/[/tan]
     [grey50]||[/grey50]      [grey50]||[/grey50]
""",
    r"""
     [green]+[/green]  [green]^^[/green]
      [green]\##/[/green]     [grey85]O==[/grey85]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][black].[/black][grey62]#######[/grey62][black].[/black][grey62]##o[/grey62]
 [tan]/#####[green]\_/[/green][tan]######\[/tan]
 [tan]\##############/[/tan]
    [grey50]||[/grey50]        [grey50]||[/grey50]
""",
]

SUCCESS_FRAMES = [
    r"""
    [green bold]*[/green bold]   [green]^^[/green]    [green bold]*[/green bold]
      [green]/##\[/green]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][black]-[/black][grey62]#######[/grey62][black]-[/black][grey62]##o[/grey62]
 [tan]/#####[black]\_/[/black][tan]######\[/tan]
 [tan]\##############/[/tan]
   [grey50]||[/grey50]          [grey50]||[/grey50]
""",
    r"""
  [green bold]*[/green bold]       [green]^^[/green] [green bold]*[/green bold]
      [green]\##/[/green]
   [grey62]_/########\_[/grey62][green]@@@[/green]
 [grey62]/############\[/grey62][green]@@@@[/green]
[grey62]o##[/grey62][black]^[/black][grey62]#######[/grey62][black]^[/black][grey62]##o[/grey62]
 [tan]/#####[black]\_/[/black][tan]######\[/tan]
 [tan]\##############/[/tan]
      [grey50]||[/grey50]  [grey50]||[/grey50]
""",
]

SLEEPING_FRAMES = [
    r"""
        [grey50]^^[/grey50]        [grey50]Z[/grey50]
      [grey50]/##\[/grey50]     [grey50]z[/grey50]
   [grey50]_/########\_[/grey50][green4]@@@[/green4]
 [grey50]/############\[/grey50][green4]@@@@[/green4]
[grey50]o##[/grey50][grey30]-[/grey30][grey50]#######[/grey50][grey30]-[/grey30][grey50]##o[/grey50]
 [tan]/#####_########\[/tan]
 [tan]\##############/[/tan]
     [grey35]||[/grey35]      [grey35]||[/grey35]
""",
    r"""
        [grey50]^^[/grey50]      [grey50]z[/grey50]
      [grey50]\##/[/grey50]       [grey50]Z[/grey50]
   [grey50]_/########\_[/grey50][green4]@@@[/green4]
 [grey50]/############\[/grey50][green4]@@@@[/green4]
[grey50]o##[/grey50][grey30]-[/grey30][grey50]#######[/grey50][grey30]-[/grey30][grey50]##o[/grey50]
 [tan]/#####_########\[/tan]
 [tan]\##############/[/tan]
    [grey35]||[/grey35]        [grey35]||[/grey35]
""",
]

MONITORING_FRAMES = IDLE_FRAMES

MASCOT_FRAMES: dict[str, list[str]] = {
    "idle": IDLE_FRAMES,
    "monitoring": MONITORING_FRAMES,
    "scanning": SCANNING_FRAMES,
    "thinking": THINKING_FRAMES,
    "alert": ALERT_FRAMES,
    "critical": CRITICAL_FRAMES,
    "healing": HEALING_FRAMES,
    "success": SUCCESS_FRAMES,
    "sleeping": SLEEPING_FRAMES,
}
