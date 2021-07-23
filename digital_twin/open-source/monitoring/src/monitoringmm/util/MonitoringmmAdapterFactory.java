/**
 */
package monitoringmm.util;

import monitoringmm.*;

import org.eclipse.emf.common.notify.Adapter;
import org.eclipse.emf.common.notify.Notifier;

import org.eclipse.emf.common.notify.impl.AdapterFactoryImpl;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * The <b>Adapter Factory</b> for the model.
 * It provides an adapter <code>createXXX</code> method for each class of the model.
 * <!-- end-user-doc -->
 * @see monitoringmm.MonitoringmmPackage
 * @generated
 */
public class MonitoringmmAdapterFactory extends AdapterFactoryImpl {
	/**
	 * The cached model package.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected static MonitoringmmPackage modelPackage;

	/**
	 * Creates an instance of the adapter factory.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public MonitoringmmAdapterFactory() {
		if (modelPackage == null) {
			modelPackage = MonitoringmmPackage.eINSTANCE;
		}
	}

	/**
	 * Returns whether this factory is applicable for the type of the object.
	 * <!-- begin-user-doc -->
	 * This implementation returns <code>true</code> if the object is either the model's package or is an instance object of the model.
	 * <!-- end-user-doc -->
	 * @return whether this factory is applicable for the type of the object.
	 * @generated
	 */
	@Override
	public boolean isFactoryForType(Object object) {
		if (object == modelPackage) {
			return true;
		}
		if (object instanceof EObject) {
			return ((EObject)object).eClass().getEPackage() == modelPackage;
		}
		return false;
	}

	/**
	 * The switch that delegates to the <code>createXXX</code> methods.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected MonitoringmmSwitch<Adapter> modelSwitch =
		new MonitoringmmSwitch<Adapter>() {
			@Override
			public Adapter caseNamedElement(NamedElement object) {
				return createNamedElementAdapter();
			}
			@Override
			public Adapter caseMonitorableElement(MonitorableElement object) {
				return createMonitorableElementAdapter();
			}
			@Override
			public Adapter caseMOAgent(MOAgent object) {
				return createMOAgentAdapter();
			}
			@Override
			public Adapter caseMOConfig(MOConfig object) {
				return createMOConfigAdapter();
			}
			@Override
			public Adapter caseMOElement(MOElement object) {
				return createMOElementAdapter();
			}
			@Override
			public Adapter caseMOProperty(MOProperty object) {
				return createMOPropertyAdapter();
			}
			@Override
			public Adapter caseMOValue(MOValue object) {
				return createMOValueAdapter();
			}
			@Override
			public Adapter defaultCase(EObject object) {
				return createEObjectAdapter();
			}
		};

	/**
	 * Creates an adapter for the <code>target</code>.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param target the object to adapt.
	 * @return the adapter for the <code>target</code>.
	 * @generated
	 */
	@Override
	public Adapter createAdapter(Notifier target) {
		return modelSwitch.doSwitch((EObject)target);
	}


	/**
	 * Creates a new adapter for an object of class '{@link monitoringmm.NamedElement <em>Named Element</em>}'.
	 * <!-- begin-user-doc -->
	 * This default implementation returns null so that we can easily ignore cases;
	 * it's useful to ignore a case when inheritance will catch all the cases anyway.
	 * <!-- end-user-doc -->
	 * @return the new adapter.
	 * @see monitoringmm.NamedElement
	 * @generated
	 */
	public Adapter createNamedElementAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link monitoringmm.MonitorableElement <em>Monitorable Element</em>}'.
	 * <!-- begin-user-doc -->
	 * This default implementation returns null so that we can easily ignore cases;
	 * it's useful to ignore a case when inheritance will catch all the cases anyway.
	 * <!-- end-user-doc -->
	 * @return the new adapter.
	 * @see monitoringmm.MonitorableElement
	 * @generated
	 */
	public Adapter createMonitorableElementAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link monitoringmm.MOAgent <em>MO Agent</em>}'.
	 * <!-- begin-user-doc -->
	 * This default implementation returns null so that we can easily ignore cases;
	 * it's useful to ignore a case when inheritance will catch all the cases anyway.
	 * <!-- end-user-doc -->
	 * @return the new adapter.
	 * @see monitoringmm.MOAgent
	 * @generated
	 */
	public Adapter createMOAgentAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link monitoringmm.MOConfig <em>MO Config</em>}'.
	 * <!-- begin-user-doc -->
	 * This default implementation returns null so that we can easily ignore cases;
	 * it's useful to ignore a case when inheritance will catch all the cases anyway.
	 * <!-- end-user-doc -->
	 * @return the new adapter.
	 * @see monitoringmm.MOConfig
	 * @generated
	 */
	public Adapter createMOConfigAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link monitoringmm.MOElement <em>MO Element</em>}'.
	 * <!-- begin-user-doc -->
	 * This default implementation returns null so that we can easily ignore cases;
	 * it's useful to ignore a case when inheritance will catch all the cases anyway.
	 * <!-- end-user-doc -->
	 * @return the new adapter.
	 * @see monitoringmm.MOElement
	 * @generated
	 */
	public Adapter createMOElementAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link monitoringmm.MOProperty <em>MO Property</em>}'.
	 * <!-- begin-user-doc -->
	 * This default implementation returns null so that we can easily ignore cases;
	 * it's useful to ignore a case when inheritance will catch all the cases anyway.
	 * <!-- end-user-doc -->
	 * @return the new adapter.
	 * @see monitoringmm.MOProperty
	 * @generated
	 */
	public Adapter createMOPropertyAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for an object of class '{@link monitoringmm.MOValue <em>MO Value</em>}'.
	 * <!-- begin-user-doc -->
	 * This default implementation returns null so that we can easily ignore cases;
	 * it's useful to ignore a case when inheritance will catch all the cases anyway.
	 * <!-- end-user-doc -->
	 * @return the new adapter.
	 * @see monitoringmm.MOValue
	 * @generated
	 */
	public Adapter createMOValueAdapter() {
		return null;
	}

	/**
	 * Creates a new adapter for the default case.
	 * <!-- begin-user-doc -->
	 * This default implementation returns null.
	 * <!-- end-user-doc -->
	 * @return the new adapter.
	 * @generated
	 */
	public Adapter createEObjectAdapter() {
		return null;
	}

} //MonitoringmmAdapterFactory
