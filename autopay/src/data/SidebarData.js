import DashboardCustomizeIcon from '@mui/icons-material/DashboardCustomize';
import ReceiptLongIcon from '@mui/icons-material/ReceiptLong';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import PaymentsIcon from '@mui/icons-material/Payments';

export const sidebarItems = [
    {
        icon: <DashboardCustomizeIcon />,
        text: "Dashboard"
    },
    {
        icon: <ReceiptLongIcon />,
        text: "Payment History"
    },
    {
        icon: <AddCircleOutlineIcon />,
        text: "Needs"
    },
    {
        icon: <PaymentsIcon />,
        text: "Pay"
    },
    {
        icon: <SettingsOutlinedIcon />,
        text: "Settings"
    }
]