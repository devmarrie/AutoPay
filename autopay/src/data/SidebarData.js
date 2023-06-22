import DashboardCustomizeIcon from '@mui/icons-material/DashboardCustomize';
import ReceiptLongIcon from '@mui/icons-material/ReceiptLong';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import PaymentsIcon from '@mui/icons-material/Payments';


export const sidebarItems = [
    {
        icon: <PaymentsIcon />,
        text: "Pay",
        route: "/pay"
    },
    {
        icon: <AddCircleOutlineIcon />,
        text: "Needs",
        route: "/needs"
    },
    {
        icon: <DashboardCustomizeIcon />,
        text: "Dashboard",
        route: "/dashboard"
    },
    {
        icon: <ReceiptLongIcon />,
        text: "Payment History",
        route: "/history"
    },
    {
        icon: <SettingsOutlinedIcon />,
        text: "Settings",
        route: "/settings"
    }
]